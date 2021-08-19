"""
Example Python script that uses pragmail's transport module.
"""
from pragmail import Client
from pragmail.transports import save_as_html

with Client("imap.gmail.com") as client:
    client.imap4.login("user@gmail.com", "password")
    client.imap4.select("INBOX")
    response, message = client.latest_message(
        "John Smith",
    )
    save_as_html(message, "john-smith-message")
