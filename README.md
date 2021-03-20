# Backend StoreMed

## Setup

### Dependencies

```bash
pip install -r requirements.txt
```

### Enviroment Variable

Change the name of example.env to .env and replace apropriate variable with their values.
PASSWORD_SALT must be shell as it being otherise will break authentication. (Will be changed for production)

```text
SECRET_KEY=<something-random>
MONGODB_USERNAME=<username-for-DB>
MONGODB_PASSWORD=<password-for-DB>
MONGODB_HOST=<DB-domain>
PASSWORD_SALT=shell
```

## Local Deployment

## Windows

### Powershell

```powershell
$env:FLASK_APP = "app"
$env:FLASK_DEBUG = "1"
flask run
```

### CMD

```cmd
set FLASK_APP=app
set FLASK_DEBUG=1  
flask run
```

## Mac/Linux

### Bash

```bash
export FLASK_APP=app
export FLASK_DEBUG=1  
flask run
```
