import re

import pytest

import pragmail

IMAP_SERVER = "imap.gmail.com"


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

    def test_client_logout(self):
        assert self.client.logout()
