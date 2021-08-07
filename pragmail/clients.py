"""
This module contains the abstraction that will allow the user to quickly
get started with pragmail. For now, the base features that check for
messages in a specified account on an IMAP mail server can be found here
as well.
"""
from imaplib import IMAP4, IMAP4_SSL
from ssl import SSLContext, create_default_context
from typing import Any, Optional, Union

from pragmail.exceptions import _catch_exception
from pragmail.utils import (
    date_format,
    date_travel,
    imap_scheme,
    ping_host,
    server_settings,
)

TEXT_MESSSAGE = "(RFC822)"

_CommandResults = Union[tuple, tuple[Any, list[None]]]
_NoResponseData = list[None]
_ResponseData = list[Union[bytes, tuple[bytes, bytes]]]
_AnyResponseData = Union[_NoResponseData, _ResponseData]


class _Client:
    """Client base class."""

    imap4: IMAP4

    @staticmethod
    def _fetch_server_settings(host: str) -> str:
        """Fetch mail server settings."""
        url: str = ""
        serv = server_settings(host, "ES")
        setts = serv["ES"].get("settings")

        if not isinstance(setts, list):
            if "not found" in setts.lower():
                raise Exception

        for sett in setts:
            adr = sett.get("address")
            if "imap" in adr:
                url = adr

        return url

    @staticmethod
    def _fetch_url_scheme(host: str) -> str:
        """Fetch required URL scheme."""
        return imap_scheme(host)[0]

    @staticmethod
    def _check_connectivity(host: str) -> bool:
        """Check connectivity to host/server."""
        return ping_host(host)

    @staticmethod
    def _decode_search_res(
        src_uids: list[bytes],
        dat_uids: list[bytes],
    ) -> tuple[list[str], list[str]]:
        """Convert a list of bytes to a list of string object."""
        src = [str(src.decode()) for src in src_uids]
        dat = [str(dat.decode()) for dat in dat_uids]
        return src, dat

    @_catch_exception
    def _search(self, criterion: str) -> _CommandResults:
        """Private method similar to `IMAP4.search` but the charset is
        specified in the request to the server.
        """
        return self.imap4.search(None, criterion)

    @_catch_exception
    def _fetch(
        self,
        msg_set: str,
        msg_parts: str,
    ) -> tuple[str, _AnyResponseData]:
        """Private method used to shorten internal calls to
        `IMAP4.fetch`.
        """
        return self.imap4.fetch(msg_set, msg_parts)

    @_catch_exception
    def logout(self) -> bool:
        """Similar to `IMAP4.logout` but also calls `IMAP4.close`, which
        sends a `CLOSE` command to the server, and is guaranteed to
        almost always work.
        """
        if self.imap4.state == "SELECTED":
            self.imap4.close()

        if self.imap4.state != "LOGOUT":
            self.imap4.logout()

        return True

    @_catch_exception
    def latest_message(
        self,
        sender: str,
        date_range: int = -1,
        message_parts: str = TEXT_MESSSAGE,
    ) -> tuple[str, _AnyResponseData]:
        """Convenience method for retrieving the latest message from
        a specified sender.

        Use the largest UID to get the most recent message. Since the
        search key `ON` command cannot guarantee a result, this method
        uses `SENTSINCE` and the days prior today —represented by
        negative integers.

        Args:
            sender (str): String contained in the envelope structure's
                FROM field.
            date_range (int, optional): Time frame or days in which a
                message is expected to be present. Defaults to -1.
            message_parts (str, optional): Message data item names.
                Defaults to TEXT_MESSSAGE (RFC822/BODY[]).

        Raises:
            Exception: Raised when date_range is greater than -1.
            Exception: No message was found from specified sender.

        Returns:
            tuple[str, _AnyResponseData]: IMAP response type and the
                message data.
        """
        if date_range > -1:
            raise Exception(
                f"date_range can't be greater than -1: \
                {date_range}"
            )

        latest_uid = 0
        sentsince = date_format(date_travel(date_range))
        src, dat = self._decode_search_res(
            self._search(f'(FROM "{sender}")')[1],
            self._search(f"(SENTSINCE {sentsince})")[1],
        )

        for uid in dat[0].split(" "):
            _uid = int(uid)
            if uid in src[0].split(" "):
                # Since UIDs are incremented, its length is relative to
                # the message's freshness; the larger the UID, the more
                # recent the message.
                if _uid > latest_uid:
                    latest_uid = _uid

        if latest_uid > 0:
            return self._fetch(str(latest_uid), message_parts)

        raise Exception(f"Message not found: {latest_uid}")

    @_catch_exception
    def __enter__(self):
        return self

    @_catch_exception
    def __exit__(self, exc_type, exc_value, trace):
        if self.imap4.state == "LOGOUT":
            return

        try:
            self.imap4.logout()
        except OSError:
            pass

        if exc_type:
            print(f"exc_type: {exc_type}")
            print(f"exc_value: {exc_value}")
            print(f"exc_traceback: {trace}")


class Client(_Client):
    """Readonly client connection to mail server.

    Based on `imaplib.IMAP4`, allowing a certain degree of user
        flexibility.

    For more information and further usage, visit:
    - https://docs.python.org/3/library/imaplib.html
    - https://datatracker.ietf.org/doc/html/rfc2060.html
    """

    def __init__(
        self,
        host: str,
        port: int = 993,
        ssl_context: Optional[SSLContext] = None,
        timeout: float = 5.0,
    ) -> None:
        """
        Args:
            host (str): The service's domain name, IMAP server URL or
                user email.
            port (int, optional): IMAP port (e.g. 143). Defaults to 993.
            ssl_context (Optional[SSLContext], optional): Client SSL
                Context. If `None`, pragmail uses
                    `ssl.create_default_context`
            timeout (float, optional): Connection timeout. Defaults to 5.0.
        """
        if "@" in host:
            host = self._fetch_server_settings(host)
        elif "imap" not in host:
            host = self._fetch_url_scheme(host)
            if not self._check_connectivity(host):
                raise Exception("Name or service not known.")

        if port == 993:
            ssl_context = create_default_context()

        self.host = host
        self.port = port
        self.ssl_context = ssl_context
        self.timeout = timeout

        if self.ssl_context is not None:
            self.imap4 = IMAP4_SSL(
                host=host,
                port=port,
                ssl_context=ssl_context,
                timeout=timeout,
            )
        else:
            self.imap4 = IMAP4(
                host=host,
                port=port,
                timeout=timeout,
            )

    def __repr__(self) -> str:
        class_repr = (
            "Client(host={host}, port={port}, "
            "ssl_context={ssl_context}, timeout={timeout}"
        )

        return class_repr.format(
            host=self.host,
            port=self.port,
            ssl_context=self.ssl_context,
            timeout=self.timeout,
        )
