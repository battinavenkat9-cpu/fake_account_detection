# AI-Powered Fake Account Detection on Social Media

A Django + machine-learning academic demonstration based on the project report provided by the team. It accepts manually entered account signals, computes derived features, predicts a demo classification, stores each result in SQLite, and shows a dashboard/history page.

## Important limitation

**This is a runnable educational prototype, not a validated real-world detector.** The model is trained on generated synthetic examples whose labels are produced from illustrative heuristics. Its holdout score measures agreement with those generated labels only; it does not establish accuracy on real social-media accounts. The app does not connect to, scrape, or take action on Instagram, Facebook, or X. Never automatically block or accuse an account based on this demo score.

## Technologies

- Python and Django
- HTML, CSS, Bootstrap 5, JavaScript
- NumPy, Pandas (listed for the project environment), scikit-learn
- SQLite

## Features

- Dashboard and analysis form
- Random Forest classification using account age, followers, following, post count, bio length, profile-picture indicator, posting rate, and follower/following ratio
- Risk-score visualization and explanatory limitation notice
- SQLite history of analyses
- Django admin support
- About page with project team and guide details

## Requirements

- Python 3.10 or newer (Python 3.11 or 3.12 recommended)
- Internet connection for Bootstrap/font CDN resources on the pages

## Setup on Windows

Open Command Prompt or the VS Code terminal inside this folder and run:

```bat
py -m venv .venv
.venv\Scriptsctivate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py train_detector
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

If `py` is not recognized, use `python` instead. If activation is blocked in PowerShell, use Command Prompt or run the environment's Python directly.

## Setup on macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py train_detector
python manage.py runserver
```

Open http://127.0.0.1:8000/.

## Project structure

```text
fake_account_detection/
├── manage.py
├── requirements.txt
├── README.md
├── config/                 # Django settings and URLs
└── detector/
    ├── models.py            # Saved analyses
    ├── forms.py             # Input validation
    ├── views.py             # Dashboard, prediction, history
    ├── ml/detector.py       # Synthetic demo training and prediction
    ├── management/commands/train_detector.py
    ├── templates/detector/  # HTML templates
    └── static/detector/     # CSS and JavaScript
```

## Team details from the supplied presentation

**Project:** AI-Powered Fake Account Detection on Social Media  
**Institution:** Indira Institute of Technology & Science, Department of CSE  
**Academic years:** 2022–2026  
**Guide:** Mr. K Surendra Reddy (M.Tech), Associate Professor

- Cheekatipalli Pooja — 227Z1A4311
- Banka Narendra Kumar Reddy — 227Z1A4308
- **Battina Venkata Subbaiah — 227Z1A4309**
- Bavannagari Ravi Kumar — 227Z1A4310
- Degala Hemanth Kumar — 227Z1A4312

## Before using with real data

1. Obtain a properly licensed dataset with reliable human-verified labels.
2. Split by user/time/source to reduce leakage and measure precision, recall, F1, confusion matrix, and false-positive rate.
3. Compare models (for example, Random Forest, SVM, and Naive Bayes) on the same split.
4. Document dataset provenance, limitations, and bias checks.
5. Add authentication, access controls, logging, privacy protections, production settings, and security review before deployment.

## GitHub upload

Create a repository with a clear name such as `ai-fake-account-detection`. Upload the project files, including `README.md` and `.gitignore`. Do not upload virtual environments, database files, secrets, or real personal account data.
