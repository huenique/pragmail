"""
Example Python script that retrieves email messages from Gmail's IMAP
server using pragmail.
"""
import re

from pragmail import Client, utils


def extract_mime_url(_message: bytes) -> list:
    """Extract URLs from message."""
    uri = []

    # Omit escape characters before parsing.
    _message = _message.replace(b"\r\n", b"")

    # Parse message body.
    body = utils.read_message(_message, as_string=True)

    if not isinstance(body, str):
        body = str(body)

    # Extract URLs. Only include link to articles written by Medium users.
    # Path to user profiles includes an "@" symbol and have greater than three
    # slashes.
    for href in re.findall(r'href=3D[\'"]?([^\'">?]+)', body):
        if href.count("/") > 3 and "@" in href:
            uri.append(href.replace("=", ""))

    return uri


def get_medium_daily_digest():
    """Retrieve relevant content URLs from the latest Medium Daily Digest
    message.
    """
    with Client("imap.gmail.com") as client:
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
