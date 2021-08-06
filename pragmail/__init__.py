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
from . import utils
from .__version__ import __version__
from .clients import Client
from .exceptions import CommandError, IMAP4Error

__url__ = "https://github.com/huenique/pragmail"
__author__ = "Hju Kneyck (hjucode@gmail.com)"
__license__ = "MIT"
