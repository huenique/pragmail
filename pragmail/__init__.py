# flake8: noqa: F401
"""
pragmail
~~~~~~~~

Example usage:
>>> import pragmail
>>> client = pragmail.Client("imap.domain.com")
>>> client.imap4.login("username", "password")
('OK', [b'username authenticated (Success)'])
>>> client.imap4.select("INBOX")
('OK', [b'1357'])
>>> client.imap4.search(None, 'FROM', '"John Smith"')
('OK', [b'245 248 257 259'])
>>> client.imap4.close()
('OK', [b'Returned to authenticated state. (Success)'])
>>> client.imap4.logout()
('BYE', [b'LOGOUT Requested'])
"""
from pragmail import utils
from pragmail.__version__ import __version__
from pragmail.clients import Client
from pragmail.exceptions import CommandError, IMAP4Error
from pragmail.transports import TransportUtils, save_to_disk

__url__ = "https://github.com/huenique/pragmail"
__author__ = "Hju Kneyck (hjucode@gmail.com)"
__license__ = "MIT"
