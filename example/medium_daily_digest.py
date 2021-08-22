"""
Example Python script that retrieves email messages from Gmail's IMAP
server using pragmail.
"""
import re

import pragmail
from pragmail import utils


def extract_mime_url(_message: bytes) -> list:
    """Extract URLs from message."""
    uri = []

    # Omit escape characters before parsing.
    _message = _message.replace(b"\r\n", b"")

    # Parse message body.
    body = utils.read_message(_message, as_string=True)

    # Extract URLs.
    if isinstance(body, str):
        hrefs = re.findall(r'href=3D[\'"]?([^\'">?]+)', body)

        # Only include link to articles written by Medium users. Path to user
        # profiles includes an `@` symbol and have less that three slashes.
        for href in hrefs:
            if href.count("/") > 3 and "@" in href:
                uri.append(href.replace("=", ""))

    return uri


def get_medium_daily_digest():
    """Retrieve relevant content URLs from the latest Medium Daily Digest
    message.
    """
    with pragmail.Client("imap.gmail.com") as client:
        client.login("user@gmail.com", "password")
        client.select("INBOX")
        response, message = client.latest_message("Medium Daily Digest")

    if response == "OK":
        message_body = message[0][1]
        articles = extract_mime_url(message_body)
    else:
        articles = []

    if articles:
        for url in articles:
            print(url)


if __name__ == "__main__":
    get_medium_daily_digest()
