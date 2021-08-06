from pragmail import CommandError, IMAP4Error


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
