# Django Projects

Ten local **Django** web apps. Each one uses SQLite, HTML templates, and Django's test client. No paid APIs.

These apps are for local use. Do not expose them publicly as-is.

## Projects

| # | Project | What it does |
| --- | --- | --- |
| 1 | [blog-site](blog-site/) | Blog posts |
| 2 | [todo-list](todo-list/) | Tasks you can complete |
| 3 | [notes-app](notes-app/) | Notes CRUD |
| 4 | [poll-app](poll-app/) | Voting poll |
| 5 | [bookstore](bookstore/) | Book catalog and search |
| 6 | [inventory](inventory/) | Stock and sales |
| 7 | [url-shortener](url-shortener/) | Short links |
| 8 | [recipe-book](recipe-book/) | Recipes |
| 9 | [student-registry](student-registry/) | Student roster |
| 10 | [issue-tracker](issue-tracker/) | Open and close issues |

## Quick start

```powershell
cd D:\AI-Agents\Django-Projects\blog-site
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

Open http://127.0.0.1:8000

```powershell
python manage.py test
```
