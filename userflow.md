Userflow

1. User signup
POST auth/users/
```json
{
  "email": "user@example.com",
  "password": "string"
}
```

2. User confirms email by clicking link
POST auth/users/activation/
```json
{
  "uid": "string",
  "token": "string"
}
```
openchaver.com/activate/[uid]/[token]
<!-- /auth/users/activation/{uid}/{token} send token backend -->

2a. User requests another confirmation email
POST auth/users/resend_activation/
```json
{
  "email": "user@example.com"
}
```

3. Log user in
POST auth/token/login/
```json
{
  "password": "string",
  "email": "string"
}
```

3a. Log user out
POST auth/token/logout/

4. User adds a device *
POST /devices/
```json
{
  "name": "string"
}
```

5. Assign device to a chaver (possibly with groups) *
POST /chavers/
```json
{
  "name": "string",
  "email": "user@example.com"
}
```


Authorization: `Token {token}`

// change email or password

client -> turn on; asks for device id
---
Add a device
Send {...Name_of_device}
returns with device info with an {uid}

Add chavers
---
{
  "name": "string",
  "email": "user@example.com",
  "device": "uuid"
}

// delete/remove chaver

DELETE /chavers/{id}/