# Poll App

Create a question and vote on choices.

Local Django app with SQLite. Do not expose it publicly as-is.

## Run

```powershell
cd D:\AI-Agents\Django-Projects\poll-app
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

## Tests

```powershell
python manage.py test
```
