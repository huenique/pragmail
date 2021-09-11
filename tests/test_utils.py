import datetime
import os
from urllib.error import HTTPError

import pytest

from pragmail import utils

IMAP_SERVER = "imap.gmail.com"
FAKE_IMAP_SERVER = "imap.fakeimapserver.com"
DOMAIN_NAME = "gmail"
KNOWN_USER_EMAIL = "example@gmail.com"
UNKNOWN_USER_EMAIL = "example@unknown.com"
TEST_FILE_BIN = "test_file.bin"
TEST_FILE_TXT = "test_file.txt"


class TestPing:
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


def test_sanitize_invalid_chars():
    assert utils.sanitize("A/B/C") == "ABC"
    assert utils.sanitize("A*C.d") == "AC.d"


def test_sanitize_invalid_suffix():
    assert utils.sanitize("def.") == "def"
    assert utils.sanitize("def.ghi") == "def.ghi"
    assert utils.sanitize("Z" * 1000 + ".").endswith("Z")


def test_sanitize_reserved_words():
    assert utils.sanitize("NUL") == "__NUL"
    assert utils.sanitize("..") == "__"


def test_sanitize_long_names():
    fname_100 = utils.sanitize(".".join(["Z" * 100, "Z" * 100, "Z" * 100]))
    fname_300 = utils.sanitize(".".join(["Z" * 300, "Z" * 300, "Z" * 300]))
    assert len(fname_100) == 255
    assert len(fname_300) == 255
    assert len(utils.sanitize("Z" * 300)) == 255
    assert len(utils.sanitize("." * 300 + ".txt")) == 255


def test_sanitize_unicode_normalization():
    assert utils.sanitize("ў") == chr(1091) + chr(774)


def test_sanitize_extensions():
    long_name = "Z" * 1000 + ".txt"
    fn_100_with_ext = "Z" * 100 + "." + "Z" * 100 + ".txt"
    fn_400_with_ext = "Z" * 100 + "." + "Z" * 400 + ".txt"
    assert utils.sanitize(long_name).endswith(".txt")
    assert utils.sanitize(fn_100_with_ext).endswith(".txt")
    assert utils.sanitize(fn_400_with_ext).endswith(".txt")
    assert utils.sanitize("Z" * 1000).endswith("Z")
    assert utils.sanitize("Z" * 100 + "." + "Z" * 400).endswith("Z")
