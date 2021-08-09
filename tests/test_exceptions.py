import pytest

from pragmail import CommandError, IMAP4Error
from pragmail.exceptions import _catch_exception


class TestIMAP4Error:
    def test_imap4_error_has_base_error(self):
        assert issubclass(CommandError, Exception)

    def test_imap4_error(self):
        ie = IMAP4Error("foo")
        assert "foo" in str(ie)


class TestCommandError:
    def test_command_error_has_attr_error(self):
        assert issubclass(CommandError, AttributeError)

    def test_command_error_has_val_error(self):
        assert issubclass(CommandError, ValueError)

    def test_command_error(self):
        ce = CommandError("foo")
        assert "foo" in str(ce)


def test_catch_exception_raises_IMAP4Error():
    @_catch_exception
    def raise_error():
        raise Exception("error raised!")

    with pytest.raises(IMAP4Error, match="error raised!"):
        raise_error()


def test_catch_exception_raises_CommandError_by_AttributeError():
    @_catch_exception
    def raise_error():
        raise AttributeError

    with pytest.raises(CommandError):
        raise_error()


def test_catch_exception_raises_CommandError_by_ValueError():
    @_catch_exception
    def raise_error():
        raise ValueError

    with pytest.raises(CommandError):
        raise_error()
