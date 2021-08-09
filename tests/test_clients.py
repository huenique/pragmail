import re

import pytest

import pragmail

CLIENT = pragmail.Client
IMAP_SERVER = "imap.gmail.com"
KNOWN_USER_EMAIL = "example@gmail.com"


class TestClient:
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

    def test_logout(self):
        assert self.client.logout()

    def test_latest_message_raises(self):
        with pytest.raises(Exception):
            self.client.latest_message("John Smith", 0)


def test_fetch_server_settings():
    fetch_server_settings = CLIENT._fetch_server_settings
    assert fetch_server_settings(KNOWN_USER_EMAIL) == IMAP_SERVER


def test_fetch_url_scheme():
    fetch_url_scheme = CLIENT._fetch_url_scheme
    assert fetch_url_scheme("gmail") == "imap://" + IMAP_SERVER


def test_check_connectivity():
    check_connectivity = CLIENT._check_connectivity
    assert isinstance(check_connectivity(IMAP_SERVER), bool)


def test_decode_search_res():
    decode_search_res = CLIENT._decode_search_res
    byte_list = [b"0"]
    byte_list_decoded = list(byte_list[0].decode())
    assert decode_search_res(byte_list, byte_list) == (
        byte_list_decoded,
        byte_list_decoded,
    )
