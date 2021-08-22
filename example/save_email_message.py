"""
Example Python script that uses pragmail's transport module.
"""
from pragmail import Client
from pragmail.transports import save_to_disk

with Client("imap.gmail.com") as client:
    client.login("user@gmail.com", "password")
    client.select("INBOX")
    response, message = client.latest_message(
        "John Smith",
    )
    save_to_disk(message, "Content of John's Email.txt")
