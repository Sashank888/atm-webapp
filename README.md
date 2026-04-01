# ATM Web App

A Flask-based ATM web application with registration, login, balance inquiry, withdrawal, deposit, transfer, and mini-statement features.

## Setup

1. Copy `.env.example` to `.env`.
2. Update `.env` with your MySQL credentials.
3. Create and activate your Python virtual environment.
4. Install dependencies:

```powershell
pip install -r requirements.txt
```

5. Run the app:

```powershell
python app.py
```

6. Open in browser:

- Local: `http://127.0.0.1:5000`
- Network: `http://<your-ip>:5000` if running with `host="0.0.0.0"`

## Notes

- Do not commit `.env`, it contains sensitive credentials.
- The `.gitignore` file is already configured to exclude `.env` and `.venv`.
