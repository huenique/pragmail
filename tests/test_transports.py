import os
import shutil
from email.message import EmailMessage, Message, MIMEPart
from pathlib import Path

import pytest

from pragmail import TransportUtils, save_to_disk

# fmt: off
MIME_MESSAGE_ATTM = (
                    'From: Some One <someone@example.com>\n'
                    'MIME-Version: 1.0\n'
                    'Content-Type: multipart/mixed; '
                    'boundary="XXXXboundary text"\n'
                    '\n'
                    'This is a multipart message in MIME format.\n'
                    '\n'
                    '--XXXXboundary text\n'
                    'Content-Type: text/plain;\n'
                    'Content-Disposition: attachment; '
                    'filename="test.txt"\n'
                    '\n'
                    'this is the attachment text'
                    '\n'
                    '--XXXXboundary text--'
                    )

MIME_MESSAGE_ATTM_BUFFER = (
                            'From: Some One <someone@example.com>\n'
                            'MIME-Version: 1.0\n'
                            'Content-Type: multipart/mixed; '
                            'boundary="XXXXboundary text"\n'
                            '\n'
                            'This is a multipart message in MIME format.\n'
                            '\n'
                            '--XXXXboundary text\n'
                            'Content-Type: application/octet-stream;\n'
                            'Content-Disposition: attachment; '
                            'filename="test.txt"\n'
                            '\n'
                            'this is the attachment text'
                            '\n'
                            '--XXXXboundary text--'
                            )

MIME_MESSAGE = (
                'From: Some One <someone@example.com>\n'
                'MIME-Version: 1.0\n'
                'Content-Type: multipart/mixed; '
                'boundary="XXXXboundary text"\n'
                '\n'
                'This is a multipart message in MIME format.\n'
                '\n'
                '--XXXXboundary text\n'
                'Content-Type: text/plain\n'
                '\n'
                'this is the body text\n'
                '\n'
                '--XXXXboundary text\n'
                'Content-Type: text/plain;\n'
                'Content-Disposition: attachment; filename="test.txt"\n'
                '\n'
                'this is the attachment text'
                '\n'
                '--XXXXboundary text--'
                )
# fmt: on


# Define paths for test generated files.
CWD = os.getcwd()
TPATH = os.path.join(CWD, "tests")
FPATH = os.path.join(CWD, "tests", "test.txt")


class TestTransportUtils(TransportUtils):

    resp_bytes_list = [b"data"]
    resp_tuple_list = [(b"data", b"data")]

    def test_data_as_bytes_bytes_list_returns_bytes(self):
        assert self.data_as_bytes(self.resp_bytes_list) == b"data"

    def test_data_as_bytes_tuple_list_returns_bytes(self):
        assert self.data_as_bytes(self.resp_tuple_list) == b"data"

    def test_data_as_bytes_invalid_type_raises(self):
        with pytest.raises(TypeError):
            self.data_as_bytes([None])

    def test_read_message_returns_emailmessage(self):
        msg = self.read_message(b"message data")
        assert isinstance(msg, EmailMessage)

    def test_read_message_returns_mimepart(self):
        msg = self.read_message(b"message data", _class=MIMEPart)
        assert isinstance(msg, MIMEPart)

    def test_read_message_returns_basicmessage(self):
        msg = self.read_message(b"message data", _class=Message)
        assert isinstance(msg, Message)

    def test_read_message_accepts_response_type(self):
        msg = self.read_message([(b"response type", b"response data")])
        assert isinstance(msg, EmailMessage)

    def test_read_message_raises_type_error(self):
        invalid_types = (
            1,
            1.0,
            1j,
            (None),
            range(1),
            {"resp": "resp"},
            {"resp"},
            frozenset({"resp"}),
            True,
            bytearray(1),
            memoryview(bytes(1)),
        )
        for typ in invalid_types:
            with pytest.raises(TypeError):
                self.read_message(typ, _class=Message)

    def test_xtract_attachments_returns_dict(self):
        attm = self.xtract_attachments(self.read_message(MIME_MESSAGE))
        expected_info = {
            "attachment_0": {
                "ctype": "text/plain",
                "filename": "test.txt",
                "buffer": "this is the attachment text",
            }
        }
        assert attm == expected_info

    def test_xtract_headers_returns_list(self):
        msg = self.read_message(MIME_MESSAGE.encode())
        hed = self.xtract_headers(msg)
        expctd = [
            ("From", "Some One <someone@example.com>"),
            ("MIME-Version", "1.0"),
            ("Content-Type", 'multipart/mixed; boundary="XXXXboundary text"'),
        ]
        assert hed == expctd

    def test_xtract_payload_returns_content(self):
        msg = self.read_message(MIME_MESSAGE.encode())
        cont = str(self.xtract_payload(msg))
        expctd = "Content-Type: text/plain\n" "\n" "this is the body text\n"
        assert cont == expctd

    def test_xtract_payload_returns_none(self):
        msg = self.read_message(MIME_MESSAGE_ATTM)
        cont = self.xtract_payload(msg)
        assert cont is None

    def test_save_attachments_text_IO(self):
        try:
            msg = self.read_message(MIME_MESSAGE)
            attm = self.xtract_attachments(msg)
            self.save_attachments(attm, TPATH)
            with open(FPATH, "r") as fp:
                assert fp.read() == "this is the attachment text"
        finally:
            dirpath = os.path.join(TPATH, "test")
            if os.path.isfile(FPATH):
                os.remove(FPATH)

            if os.path.isdir(dirpath):
                shutil.rmtree(dirpath)

    def test_save_attachments_bytes_IO(self):
        try:
            msg = self.read_message(MIME_MESSAGE_ATTM_BUFFER)
            attm = self.xtract_attachments(msg)
            self.save_attachments(attm, TPATH)
            with open(FPATH, "rb") as fp:
                assert fp.read() == b"this is the attachment text"
        finally:
            dirpath = os.path.join(TPATH, "test")
            if os.path.isfile(FPATH):
                os.remove(FPATH)

            if os.path.isdir(dirpath):
                shutil.rmtree(dirpath)

    def test_create_file_takes_str_object(self):
        try:
            self.create_file(FPATH, "file content")
            with open(FPATH, "r") as fp:
                assert fp.read() == "file content"
        finally:
            if os.path.isfile(FPATH):
                os.remove(FPATH)

    def test_create_file_takes_path_object(self):
        try:
            self.create_file(Path(FPATH), "file content")
            with open(FPATH, "r") as fp:
                assert fp.read() == "file content"
        finally:
            if os.path.isfile(FPATH):
                os.remove(FPATH)

    def test_create_file_writes_to_bytes(self):
        try:
            self.create_file(Path(FPATH), b"file content")
            with open(FPATH, "r") as fp:
                assert fp.read() == "file content"
        finally:
            if os.path.isfile(FPATH):
                os.remove(FPATH)

    def test_create_file_str_object_no_suffix(self):
        try:
            self.create_file(Path(FPATH).with_suffix(""), "file content")
            with open(FPATH, "r") as fp:
                assert fp.read() == "file content"
        finally:
            if os.path.isfile(FPATH):
                os.remove(FPATH)

    def test_create_directory_takes_str_object(self):
        try:
            self.create_directory(os.path.join(CWD, "tests", "tests"))
        finally:
            dirpath = os.path.join(TPATH, "test")
            if os.path.isdir(dirpath):
                shutil.rmtree(dirpath)


def test_save_to_disk():
    try:
        attm_fpath = os.path.join(FPATH.replace(".txt", ""), "test.txt")
        save_to_disk(MIME_MESSAGE, FPATH)
        with open(FPATH, "r") as fp:
            assert fp.read() == (
                "Content-Type: text/plain\n" "\n" "this is the body text\n"
            )
        with open(attm_fpath, "r") as fp:
            assert fp.read() == "this is the attachment text"
    finally:
        dirpath = os.path.join(TPATH, "test")
        if os.path.isfile(FPATH):
            os.remove(FPATH)

        if os.path.isdir(dirpath):
            shutil.rmtree(dirpath)
