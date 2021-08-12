"""
This module provides useful functions that facilitate pragmail's routine
operations.
"""
import calendar
import datetime
import json
import platform
from email import (
    message_from_binary_file,
    message_from_bytes,
    message_from_file,
    message_from_string,
)
from email.message import Message
from io import BufferedIOBase, TextIOBase
from subprocess import DEVNULL as _DEVNULL
from subprocess import call
from typing import Any, BinaryIO, Optional, TextIO, Union
from urllib.request import urlopen


def date_format(date_ymd: str) -> str:
    """Convert date to IMAP SEARCH Command acceptable format.

    Args:
        date_ymd (str): The date in `YYYY-MM-DD` format.

    Returns:
        str: The date in `DD-MM-YYYY` format and the month replaced with its
            abbreviated form.
    """
    date = date_ymd.split("-")[::-1]
    return f"{date[0]}-{calendar.month_abbr[int(date[1])]}-{date[2]}"


def date_travel(days: int) -> str:
    """Returns the date by day beginning from today.

    Args:
        days (int): Number of days.

    Returns:
        str: The date in `YYYY-MM-DD` format.
    """
    date = datetime.date.today() + datetime.timedelta(days=days)
    return str(date)


def email_domain(email: str) -> str:
    """Get the domain name from the email address.

    Args:
        email (str): The user email address.

    Returns:
        str: The domain name contained in the email.
    """
    return email.split("@")[1].split(".")[0]


def ping_host(host) -> bool:
    """Use the system's network utility to check if the server responds to a
    ping request.

    Args:
        host ([type]): IP address of the server or the host name.

    Returns:
        bool: [description]
    """
    plat = platform.system().lower()
    c_param = "-n" if plat == "windows" else "-c"
    c_limit = "1"
    t_param = "-w" if plat == "windows" else "-W"
    t_limit = "5000" if plat == "windows" else "5"
    command = [
        "ping",
        c_param,
        c_limit,
        t_param,
        t_limit,
        host,
    ]

    return call(command, stdout=_DEVNULL, stderr=_DEVNULL) == 0


def read_message(
    message: Union[bytes, str, BinaryIO, TextIO],
    as_string: Optional[bool] = False,
) -> Union[str, bytes]:
    """Parse email message.

    Args:
        message (Union[bytes, str, BinaryIO, TextIO]): The message object.
        as_string (Optional[bool[], optional): Parse the message object and
            return a string. Defaults to False.

    Returns:
        Union[str, bytes]: Parsed email message.
    """
    msg: Message = Message()

    if isinstance(message, bytes):
        msg = message_from_bytes(message)
    elif isinstance(message, str):
        msg = message_from_string(message)
    elif isinstance(message, BufferedIOBase):
        msg = message_from_binary_file(message)
    elif isinstance(message, TextIOBase):
        msg = message_from_file(message)

    if as_string:
        return msg.as_string()
    return msg.as_bytes()


def server_settings(email: str, provider: str) -> dict[str, Any]:
    """Fetch mail server specifications using third party services.

    Args:
        email (str): The user email address.
        provider (str): Service providing email settings lookup.

    Returns:
        dict[str, Any]: [description]
    """
    providers = {
        "ES": "https://emailsettings.firetrust.com/settings?q={email}",
    }
    with urlopen(providers[provider].format(email=email)) as res:
        src = list(p if p == provider else "" for p, _ in providers.items())[0]
        return {src: json.loads(res.read())}


def imap_scheme(domain: str) -> tuple[str, str]:
    """Convert domain name to an rfc5092-compliant IMAP URL scheme.

    Args:
        domain (str): Domain name of the service provider.

    Returns:
        tuple[str, str]: The IMAP server URL and its SSL/TLS port number.
    """
    url = f"imap.{domain}.com"
    port = "993"
    return "imap://" + url, port


if __name__ == "__main__":
    pass
