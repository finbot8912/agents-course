# Daily Journal App

This is a simple Flask web application to manage daily work and study notes. It allows you to:

- Track tasks with project name, details, progress dates and assignee.
- Record study logs with references.
- Keep meetings and memos.
- View all tasks from a dashboard.

## Setup

1. Create a Python virtual environment (optional).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

The app will create an `sqlite` database file named `journal.db` in the same directory.

## Deployment

To deploy, push the `daily_journal_app` directory to your GitHub repository and configure a platform like Heroku or Render that supports Flask applications. Ensure that the environment installs the packages from `requirements.txt` before starting `python app.py`.

