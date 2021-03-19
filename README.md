# Backend StoreMed

## Setup

### Dependencies

```bash
pip install -r requirements.txt
```

### Enviroment Variable

Change the name of example.env to .env and replace apropriate variable with their values.

```text
SECRET_KEY=<something-random>
MONGODB_USERNAME=<username-for-DB>
MONGODB_PASSWORD=<password-for-DB>
MONGODB_HOST=<DB-domain>
```

## Local Deployment

## Windows

### Powershell

```powershell
$env:FLASK_APP = "app"
flask run
```

### CMD

```cmd
set FLASK_APP=app
flask run
```

## Mac/Linux

### Bash

```bash
export FLASK_APP=app
flask run
```
