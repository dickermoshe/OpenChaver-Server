# Standard userflow

| Action                             | Frontend                                | API call                                |
| ---------------------------------- | --------------------------------------- | --------------------------------------  |
| 1.  User signup                    |`/signup`                                | POST `auth/users/`                      |
| 2.  Confirm email link             |`openchaver.com/activate/[uid]/[token]`  | POST `auth/users/activation/`           |
| 2a. Request another email link     |`/login` on:login of inactive account    | POST `auth/users/resend_activation/`    |
| 3. Login                           |`/login`                                 | POST `auth/token/login/`                |
| 3a. Logout                         |Button click                             | POST `auth/token/logout/`               |
| 4. Add a device to account         |                                         | POST `/devices/`                        |
| 5. Assign device to chaver         |                                         | POST `chavers`                          |

*Note:* From 3a and on a `Authorization: 'Token {token}'` header is required on the request.


2a. User requests another confirmation email
POST auth/users/resend_activation/
```json
{
  "email": "user@example.com"
}
```

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
