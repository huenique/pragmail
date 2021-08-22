<!-- markdownlint-disable -->

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `utils`
This module provides useful functions that facilitate pragmail's routine operations. 


---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/utils.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `date_format`

```python
date_format(date_ymd: str) → str
```

Convert date to IMAP SEARCH Command acceptable format. 



**Args:**
 
 - <b>`date_ymd`</b> (str):  The date in `YYYY-MM-DD` format. 



**Returns:**
 
 - <b>`str`</b>:  The date in `DD-MM-YYYY` format and the month replaced with its  abbreviated form. 


---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/utils.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `date_travel`

```python
date_travel(days: int) → str
```

Returns the date by day beginning from today. 



**Args:**
 
 - <b>`days`</b> (int):  Number of days. 



**Returns:**
 
 - <b>`str`</b>:  The date in `YYYY-MM-DD` format. 


---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/utils.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `email_domain`

```python
email_domain(email: str) → str
```

Get the domain name from the email address. 



**Args:**
 
 - <b>`email`</b> (str):  The user email address. 



**Returns:**
 
 - <b>`str`</b>:  The domain name contained in the email. 


---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/utils.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `ping_host`

```python
ping_host(host) → bool
```

Use the system's network utility to check if the server responds to a ping request. 



**Args:**
 
 - <b>`host`</b> ([type]):  IP address of the server or the host name. 



**Returns:**
 
 - <b>`bool`</b>:  [description] 


---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/utils.py#L89"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_message`

```python
read_message(
    message: Union[bytes, str, BinaryIO, TextIO],
    as_string: Optional[bool] = False
) → Union[str, bytes]
```

Parse email message. 



**Args:**
 
 - <b>`message`</b> (Union[bytes, str, BinaryIO, TextIO]):  The message object. 
 - <b>`as_string`</b> (Optional[bool[], optional):  Parse the message object and  return a string. Defaults to False. 



**Returns:**
 
 - <b>`Union[str, bytes]`</b>:  Parsed email message. 


---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/utils.py#L119"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `server_settings`

```python
server_settings(email: str, provider: str) → dict[str, Any]
```

Fetch mail server specifications using third party services. 



**Args:**
 
 - <b>`email`</b> (str):  The user email address. 
 - <b>`provider`</b> (str):  Service providing email settings lookup. 



**Returns:**
 
 - <b>`dict[str, Any]`</b>:  [description] 


---

<a href="https://github.com/hunique/pragmail/tree/main/pragmail/utils.py#L137"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `imap_scheme`

```python
imap_scheme(domain: str) → tuple[str, str]
```

Convert domain name to an rfc5092-compliant IMAP URL scheme. 



**Args:**
 
 - <b>`domain`</b> (str):  Domain name of the service provider. 



**Returns:**
 
 - <b>`tuple[str, str]`</b>:  The IMAP server URL and its SSL/TLS port number. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
