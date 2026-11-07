# Recipe Book

Store recipes with ingredients and steps.

Local Django app with SQLite. Do not expose it publicly as-is.

## Run

```powershell
cd D:\AI-Agents\Django-Projects\recipe-book
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
