<!-- markdownlint-disable -->

<a href="https://github.com/huenique/pragmail/blob/main/pragmail/clients.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `clients`
This module contains the abstraction that will allow the user to quickly get started with pragmail. For now, the base features that check for messages in a specified account on an IMAP mail server can be found here as well.

**Global Variables**
---------------
- **TEXT_MESSSAGE**


---

<a href="https://github.com/huenique/pragmail/blob/main/pragmail/clients.py#L181"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Client`
Readonly client connection to mail server.

Based on `imaplib.IMAP4`, allowing a certain degree of user  flexibility.

For more information and further usage, visit:
- https://docs.python.org/3/library/imaplib.html
- https://datatracker.ietf.org/doc/html/rfc2060.html

<a href="https://github.com/huenique/pragmail/blob/main/pragmail/clients.py#L192"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    host: str,
    port: int = 993,
    ssl_context: Optional[SSLContext] = None,
    timeout: float = 5.0
) → None
```



**Args:**

 - <b>`host`</b> (str):  The service's domain name, IMAP server URL or  user email.
 - <b>`port`</b> (int, optional):  IMAP port (e.g. 143). Defaults to 993.
 - <b>`ssl_context`</b> (Optional[SSLContext], optional):  Client SSL  Context. If `None`, pragmail uses  `ssl.create_default_context`
 - <b>`timeout`</b> (float, optional):  Connection timeout. Defaults to 5.0.




---

<a href="https://github.com/huenique/pragmail/blob/main/pragmail/exceptions.py#L103"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `latest_message`

```python
latest_message(
    sender: str,
    date_range: int = -1,
    message_parts: str = '(RFC822)'
) → tuple[str, Union[list[None], list[Union[bytes, tuple[bytes, bytes]]]]]
```

Convenience method for retrieving the latest message from a specified sender.

Use the largest UID to get the most recent message. Since the search key `ON` command cannot guarantee a result, this method uses `SENTSINCE` and the days prior today —represented by negative integers.



**Args:**

 - <b>`sender`</b> (str):  String contained in the envelope structure's  FROM field.
 - <b>`date_range`</b> (int, optional):  Time frame or days in which a  message is expected to be present. Defaults to -1.
 - <b>`message_parts`</b> (str, optional):  Message data item names.  Defaults to TEXT_MESSSAGE (RFC822/BODY[]).



**Raises:**

 - <b>`Exception`</b>:  Raised when date_range is greater than -1.
 - <b>`Exception`</b>:  No message was found from specified sender.



**Returns:**

 - <b>`tuple[str, _AnyResponseData]`</b>:  IMAP response type and the  message data.

---

<a href="https://github.com/huenique/pragmail/blob/main/pragmail/exceptions.py#L89"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `logout`

```python
logout() → bool
```

Similar to `IMAP4.logout` but also calls `IMAP4.close`, which sends a `CLOSE` command to the server, and is guaranteed to almost always work.




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
