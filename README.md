# pragmail [![codecov](https://codecov.io/gh/huenique/pragmail/branch/main/graph/badge.svg?token=XXYW6MUCY4)](https://codecov.io/gh/huenique/pragmail) [![python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-360/)

pragmail is a library for retrieving email messages for other useful software applications.

It's tightly based on several of Python's built-in modules for internet protocols and support, maintaining the same degree of user flexibility.

Example usage:
```python
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
```

As shown, pragmail doesn't provide unnecessary abstraction, but it does equip you with several utility functions and a few useful methods.

# Installing

pragmail can be installed with pip:
```
$ python -m pip install pragmail
```

You can get the latest source code from GitHub:
```
$ git clone git://github.com/huenique/pragmail.git
$ cd pragmail/
$ poetry install
```

# Documentation

Usage and reference documentation is found [here](https://github.com/huenique/pragmail/tree/main/docs).

# Contributing

Check the [contributing guide](https://github.com/huenique/pragmail/blob/main/.github/CONTRIBUTING.md) to learn more about the development process and how you can test your changes.
