import os
import re
from imaplib import IMAP4, IMAP4_SSL

import pytest
from dotenv import load_dotenv

import pragmail
from pragmail.clients import Client

load_dotenv()

CLIENT = pragmail.Client

IMAP_SERVER = os.getenv("IMAP_MAIL_SERVER")
KNOWN_USER_USERNAME = os.getenv("IMAP_MAIL_SERVER_USER")
KNOWN_USER_PASSWORD = os.getenv("IMAP_MAIL_SERVER_PASS")
KNOWN_SENDER = os.getenv("KNOWN_SENDER")

IMAP_SERVER_ALT = "imap.mail.com"
UKNOWN_HOST_NAME = "serviceprovider"
UKNOWN_USER_USERNAME = "example@unknown.com"


class TestClientInstance:
    """Test `pragmail.Client`'s public API.

    For methods that extend `imaplib`, we test for their return types.
    """

    client = pragmail.Client(IMAP_SERVER, 993, None, 3.0)

    def test_constructor(self):
        assert self.client.host == IMAP_SERVER
        assert self.client.port == 993
        assert self.client.ssl_context is not None
        assert self.client.timeout == 3.0

    def test_constructor_raises(self):
        with pytest.raises(Exception):
            with pragmail.Client() as client:
                client.imap4.noop()

    def test_class_representation(self):
        class_repr = repr(self.client)
        match_repr = "Client(host=imap.gmail.com, port=993, timeout=3.0"
        class_repr = re.sub(
            r"ssl_context=<ssl.SSLContext object at [\s\S]*>,",
            "",
            class_repr,
        )
        assert " ".join(class_repr.split()) == match_repr

    def test_login(self):
        assert isinstance(
            self.client.login(KNOWN_USER_USERNAME, KNOWN_USER_PASSWORD),
            tuple,
        )

    def test_select(self):
        assert isinstance(self.client.select("INBOX"), tuple)

    def test_latest_message(self):
        assert isinstance(
            self.client.latest_message(
                KNOWN_SENDER,
                date_range=-2,
                message_parts="RFC822.SIZE",
            ),
            tuple,
        )

    def test_latest_message_raises_invalid_date_range(self):
        with pytest.raises(Exception):
            self.client.latest_message("John Smith", 0)

    def test_latest_message_raises_message_not_found(self):
        # This is a randomly generate MD5 hash, which no email user is likely
        # to use.
        unknown_sender = "3f4c558a01e46b9ed6be15c3cb110f9f"
        with pytest.raises(Exception, match="Message not found: 0"):
            self.client.latest_message(unknown_sender, -1)

    def test_logout(self):
        assert self.client.logout()


def test_client_context_manager():
    with Client(IMAP_SERVER) as client:
        pass
    assert isinstance(client, Client)


def test_client_context_manger_has_imap():
    client = Client(IMAP_SERVER_ALT, port=143)
    assert isinstance(client.imap4, IMAP4)
    client.logout()


def test_client_context_manger_has_imap_ssl():
    client = Client(IMAP_SERVER_ALT)
    assert isinstance(client.imap4, IMAP4_SSL)
    client.logout()


def test_client_context_manager_prints_exec_info(capsys):
    client = Client(IMAP_SERVER)
    client.__exit__(Exception, 1, "Error traceback")
    captured = capsys.readouterr()
    assert captured.out == (
        "exc_type: <class 'Exception'>\n"
        "exc_value: 1\n"
        "exc_traceback: Error traceback\n"
        ""
    )
    client.logout()


def test_client_class_formats_at_symbol():
    client = Client(KNOWN_USER_USERNAME)
    assert client.host == IMAP_SERVER
    client.logout()


def test_client_class_formats_host_only():
    client = Client("gmail")
    assert client.host == IMAP_SERVER
    client.logout()


def test_client_class_format_raises():
    with pytest.raises(Exception, match="Name or service not known."):
        Client(UKNOWN_HOST_NAME)


def test_fetch_server_settings():
    assert CLIENT.fetch_server_settings(KNOWN_USER_USERNAME) == IMAP_SERVER


def test_fetch_url_scheme():
    assert CLIENT.fetch_url_scheme("gmail") == "imap://" + IMAP_SERVER


def test_check_connectivity():
    assert isinstance(CLIENT.check_connectivity(IMAP_SERVER), bool)


def test_decode_search_res():
    byte_list = [b"0"]
    byte_list_decoded = list(byte_list[0].decode())
    assert CLIENT.decode_search_res(byte_list) == byte_list_decoded
