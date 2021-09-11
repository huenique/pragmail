<!-- markdownlint-disable -->

# API Overview

## Modules

- [`clients`](./clients.md#module-clients): This module contains the abstraction that will allow the user to quickly get...
- [`exceptions`](./exceptions.md#module-exceptions): Implementation of custom exceptions for pragmail.
- [`transports`](./transports.md#module-transports): This module provides utilities for representing and restructuring RFC 2822 and...
- [`utils`](./utils.md#module-utils): This module provides useful functions that facilitate pragmail's routine...

## Classes

- [`clients.Client`](./clients.md#class-client): Readonly client connection to mail server.
- [`exceptions.CommandError`](./exceptions.md#class-commanderror): Exception raised when command usage is invalid.
- [`exceptions.IMAP4Error`](./exceptions.md#class-imap4error): Generic pragmail exception.
- [`transports.TransportUtils`](./transports.md#class-transportutils): Class containing methods for handling message objects.

## Functions

- [`transports.save_to_disk`](./transports.md#function-save_to_disk): Disassemble and restructure message instance as a txt file. Attachments...
- [`utils.date_format`](./utils.md#function-date_format): Convert date to IMAP SEARCH Command acceptable format.
- [`utils.date_travel`](./utils.md#function-date_travel): Returns the date by day beginning from today.
- [`utils.email_domain`](./utils.md#function-email_domain): Get the domain name from the email address.
- [`utils.imap_scheme`](./utils.md#function-imap_scheme): Convert domain name to an rfc5092-compliant IMAP URL scheme.
- [`utils.ping_host`](./utils.md#function-ping_host): Use the system's network utility to check if the server responds to a...
- [`utils.read_message`](./utils.md#function-read_message): Parse email message.
- [`utils.sanitize`](./utils.md#function-sanitize): Sanitize filenames.
- [`utils.server_settings`](./utils.md#function-server_settings): Fetch mail server specifications using third party services.


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
