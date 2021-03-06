# API Documentation

## Authentication

### Login

Path - /auth/login  
Request Type - POST  
Argument Format - JSON  

#### Arguments

&nbsp;&nbsp;email - string (required)  
&nbsp;&nbsp;password - string (required)  

#### Example

POST [https://store-med.herokuapp.com/auth/login](https://store-med.herokuapp.com/auth/login)

```json
{
    "email": "email@email.com",
    "password": "qwerty123"
}
```

#### Returns

```json
{
    "success": true
}
```

Adds JWT to cookies

### Signup

Path - /auth/signup  
Request Type - POST  
Argument Format - JSON  

#### Arguments (*subject to change*)

&nbsp;&nbsp;email - string (required)  
&nbsp;&nbsp;password - string (required)  
&nbsp;&nbsp;name - string (required)  

#### Example

POST [https://store-med.herokuapp.com/auth/signup](https://store-med.herokuapp.com/auth/signup)

```json
{
    "email": "email@email.com",
    "password": "qwerty123",
    "name": "John Doe",
}
```

#### Returns

#### Success

```json
{
    "success": true
}
```

Adds JWT to cookies

#### Error

Status Code - 400

```json
{
    "success": false,
    "error": "<prop-name> not provided"
}
```

#### Error


Status Code - 400

```json
{
    "success": false,
    "error": "Must be more than 18 years of age"
}
```

### Logout

Path - /auth/logout  
Request Type - POST  
Argument Format - JSON  

#### Arguments

None

#### Example

POST [https://store-med.herokuapp.com/auth/logout](https://store-med.herokuapp.com/auth/logout)

#### Returns

```json
{
    "success": true
}
```

Removes JWT from cookies
