import datetime
import os
from urllib.error import HTTPError

import pytest

from pragmail import utils

IMAP_SERVER = "imap.gmail.com"
FAKE_IMAP_SERVER = "imap.google.com"
DOMAIN_NAME = "gmail"
KNOWN_USER_EMAIL = "example@gmail.com"
UNKNOWN_USER_EMAIL = "example@unknown.com"
TEST_FILE_BIN = "test_file.bin"
TEST_FILE_TXT = "test_file.txt"


class TestPing:
    def test_ping_known_name(self):
        assert utils.ping_host(IMAP_SERVER) is True

    def test_ping_unknown_name(self):
        assert utils.ping_host(FAKE_IMAP_SERVER) is False


class TestReadMessage:
    nbyte_msg = b"\nmessage"
    nstr_msg = "\nmessage"
    byte_msg = b"message"
    str_msg = "message"

    def test_read_message_from_bytes(self):
        assert utils.read_message(self.byte_msg) == self.nbyte_msg

    def test_read_message_from_string(self):
        assert utils.read_message(self.str_msg) == self.nbyte_msg

    def test_read_message_from_bytes_as_string(self):
        assert utils.read_message(self.byte_msg, True) == self.nstr_msg

    def test_read_message_binary_file(self):
        with open(TEST_FILE_BIN, "wb") as fp:
            fp.write(self.byte_msg)

        with open(TEST_FILE_BIN, "rb") as fp:
            assert utils.read_message(fp) == self.nbyte_msg
            os.unlink(TEST_FILE_BIN)

    def test_read_message_text_file(self):
        with open(TEST_FILE_TXT, "a+") as fp:
            fp.write(self.str_msg)
            fp.seek(0)
            assert utils.read_message(fp) == self.nbyte_msg
            os.unlink(TEST_FILE_TXT)


class TestServerSettings:
    def test_server_settings_emailsettings_known_user(self):
        res = utils.server_settings(KNOWN_USER_EMAIL, "ES")["ES"]
        assert len(res) > 1

    def test_server_settings_emailsettings_raises_error(self):
        with pytest.raises(HTTPError):
            utils.server_settings(UNKNOWN_USER_EMAIL, "ES")["ES"]


def test_date_format():
    assert utils.date_format("2021-01-01") == "01-Jan-2021"


@pytest.mark.parametrize(
    "day,expected",
    [
        (
            1,
            str(datetime.date.today() + datetime.timedelta(days=1)),
        ),
        (
            -1,
            str(datetime.date.today() + datetime.timedelta(days=-1)),
        ),
        (
            1000,
            str(datetime.date.today() + datetime.timedelta(days=1000)),
        ),
        (
            -1000,
            str(datetime.date.today() + datetime.timedelta(days=-1000)),
        ),
    ],
)
def test_date_travel(day, expected):
    assert utils.date_travel(day) == expected


def test_email_domain():
    assert utils.email_domain(KNOWN_USER_EMAIL) == DOMAIN_NAME


def test_imap_scheme():
    assert utils.imap_scheme(DOMAIN_NAME)
