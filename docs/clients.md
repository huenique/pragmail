<!-- markdownlint-disable -->

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/clients.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `clients`
This module contains the abstraction that will allow the user to quickly get started with pragmail. For now, the base features that check for messages in a specified account on an IMAP mail server can be found here as well. 

**Global Variables**
---------------
- **TEXT_MESSSAGE**


---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/clients.py#L220"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Client`
Readonly client connection to mail server. 

Based on `imaplib.IMAP4`, allowing a certain degree of user flexibility. 

For more information and further usage, visit: 
- https://docs.python.org/3/library/imaplib.html 
- https://datatracker.ietf.org/doc/html/rfc2060.html 

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/clients.py#L230"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
 
 - <b>`host`</b> (str):  The service's domain name, IMAP server URL or user  email. 
 - <b>`port`</b> (int, optional):  IMAP port (e.g. 143). Defaults to 993. 
 - <b>`ssl_context`</b> (Optional[SSLContext], optional):  Client SSL Context.  If `None`, pragmail uses `ssl.create_default_context` 
 - <b>`timeout`</b> (float, optional):  Connection timeout. Defaults to 5.0. 




---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/clients.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `check_connectivity`

```python
check_connectivity(host: str) → bool
```

Check connectivity to host/server. 



**Args:**
 
 - <b>`host`</b> (str):  The host property of the URL interface. 



**Returns:**
 
 - <b>`bool`</b>:  True if host is reachable, False otherwise. 

---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/clients.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `decode_search_res`

```python
decode_search_res(uids: list) → list[str]
```

Convert a list of bytes to a list of string object. 



**Args:**
 
 - <b>`src_uids`</b> (list[bytes]):  A list of UIDs returned by the IMAP mail  server. 
 - <b>`dat_uids`</b> (list[bytes]):  [description] 



**Returns:**
 
 - <b>`tuple[list[str], list[str]]`</b>:  [description] 

---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/clients.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `fetch_server_settings`

```python
fetch_server_settings(user: str) → str
```

Fetch mail server settings. 



**Args:**
 
 - <b>`user`</b> (str):  The user's complete email. 



**Raises:**
 
 - <b>`Exception`</b>:  If the mail server or its settings cannot be  identified. 



**Returns:**
 
 - <b>`str`</b>:  The mail server's URL. 

---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/clients.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `fetch_url_scheme`

```python
fetch_url_scheme(domain_name: str) → str
```

Fetch desired URL scheme. 



**Args:**
 
 - <b>`host`</b> (str):  The service's domain name. 



**Returns:**
 
 - <b>`str`</b>:  URL scheme. 

---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/exceptions.py#L146"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
 
 - <b>`sender`</b> (str):  String contained in the envelope structure's FROM  field. 
 - <b>`date_range`</b> (int, optional):  Time frame or days in which a message  is expected to be present. Defaults to -1. 
 - <b>`message_parts`</b> (str, optional):  Message data item names. Defaults  to TEXT_MESSSAGE (RFC822/BODY[]). 



**Raises:**
 
 - <b>`Exception`</b>:  Raised when date_range is greater than -1. 
 - <b>`Exception`</b>:  No message was found from specified sender. 



**Returns:**
 
 - <b>`tuple[str, _AnyResponseData]`</b>:  IMAP response type and the message  data. 

---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/exceptions.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `login`

```python
login(username: str, password: str) → tuple[Literal['OK'], list[bytes]]
```

Identify the client and authenticate the user using plaintext password. 



**Args:**
 
 - <b>`username`</b> (str):  The user's username. 
 - <b>`password`</b> (str):  The user's password. 



**Raises:**
 
 - <b>`Exception`</b>:  Raised if username or password was rejected. 



**Returns:**
 
 - <b>`tuple[Literal['OK'], list[bytes]]`</b>:  Non-specific response. 

---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/exceptions.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `logout`

```python
logout() → bool
```

Similar to `IMAP4.logout` but also calls `IMAP4.close`, which  sends a `CLOSE` command to the server, and is guaranteed to  almost always work. 



**Returns:**
 
 - <b>`bool`</b>:  True for success, False otherwise. 

---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/exceptions.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `select`

```python
select(mailbox: str) → tuple[str, list[Optional[bytes]]]
```

Select a mailbox so that messages in the mailbox can be accessed. 



**Args:**
 
 - <b>`mailbox`</b> (str):  Mailbox name. 



**Returns:**
 
 - <b>`tuple[str, list[Union[bytes, None]]]`</b>:  The response type and count  of messages in the specified mailbox. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
