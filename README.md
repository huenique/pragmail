# pragmail [![python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-360/)

pragmail is a library for retrieving email messages for other useful software applications.

It extends Python's built-in modules for internet protocols and support, maintaining the same degree of user flexibility.

Example usage:
```python
>>> import pragmail
>>> client = pragmail.Client("imap.domain.com")
>>> client.login("username", "password")
('OK', [b'username authenticated (Success)'])
>>> client.select("INBOX")
('OK', [b'1357'])
>>> client.imap4.search(None, 'FROM', '"John Smith"')
('OK', [b'245 248 257 259'])
>>> client.imap4.close()
('OK', [b'Returned to authenticated state. (Success)'])
>>> client.imap4.logout()
('BYE', [b'LOGOUT Requested'])
```

pragmail also equips you with several utility functions and a few useful methods for managing retrieved email messages. Please refer to the documentation for details.

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

Usage and reference documentation is found [here](./docs).

# Contributing

Check the [contributing guide](./.github/CONTRIBUTING.md) to learn more about the development process and how you can test your changes.
