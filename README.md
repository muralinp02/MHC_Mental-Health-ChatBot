# MHC_Mental-Health-ChatBot
A conversational AI chatbot designed to provide mental health support, active listening, and general well-being guidance. Built with a focus on empathy, privacy, and accessibility, the chatbot offers resources, coping strategies, and mood tracking to assist users in managing their mental health.


> **Academic Project @ AEC**
> **Aim:** Educate users with accurate mental-health information and provide wellness utilities (mindfulness, journaling, screening) — **not for diagnosis**.
> **Duration:** \~1.5 months  |  **Grade:** A+

## ✨ Features

* Register, Login, or **Continue as Guest** (privacy-first)
* Chat with the chatbot (rule/ML-assisted responses)
* Topic-based guidance (stress, anxiety, habits, etc.)
* Mental health **self-assessments** (screeners; not diagnostic)
* **Mindfulness exercises** (guided breathing, grounding)
* **Journaling** for manual tracking
* **SOS Hotlines (India)**
* Edit profile

## 🧰 Tech Stack

* **Frontend:** Flask templates + **Bootstrap** (HTML/CSS/JS)
* **Backend:** **Python (Flask)**
* **Database:** **MySQL** via **SQLAlchemy**
* **ML/NLP:** **TensorFlow**, **NLTK**
* Auth & security: `flask-login`, `flask-bcrypt`

## 📦 Installation

### 1) Clone

```bash
git clone <your-repo-url>.git
cd <repo-folder>
```

### 2) Create & activate virtual env (Python 3.8+)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure app

Create `config.py` in the project root (or set environment variables):

```python
# config.py
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")  # use a strong secret in prod
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        "mysql+pymysql://username:password@localhost:3306/mhc_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ML/NLP specific
    NLTK_DATA_DIR = os.getenv("NLTK_DATA_DIR", "")
```

Tips:

* Generate a strong key:

  ```bash
  python -c "import secrets; print(secrets.token_hex(32))"
  ```
* Example URI:

  ```
  mysql+pymysql://root:YOURPASSWORD@127.0.0.1:3306/mhc_db
  ```

### 5) Initialize the database

Create the database in MySQL (once):

```sql
CREATE DATABASE mhc_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

If you don’t use migrations, you can quickly create tables with a helper script:

```python
# scripts/init_db.py
from app import create_app, db  # ensure create_app() returns Flask app
app = create_app()
with app.app_context():
    db.create_all()
    print("Tables created.")
```

Run:

```bash
python scripts/init_db.py
```

### 6) Download NLTK data (common corpora)

```bash
python -m nltk.downloader punkt stopwords wordnet
```

### 7) Run the app

```bash
python run.py
# or, if using flask cli:
# set FLASK_APP=run.py (Windows) | export FLASK_APP=run.py (macOS/Linux)
# flask run
```

The app should be available at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


## 🧠 ML/NLP Notes

* **TensorFlow** model for intent classification / response ranking.
* **NLTK** for tokenization, lemmatization, and simple heuristics.
* You can cache the model under `app/services/` and load once on startup.

## 🔒 Safety & Ethics

* **Not a medical device.** Provides education, coping skills, and resources only.
* **No diagnosis or treatment.** For emergencies in India, call your local helpline.
* **Guest Mode** available to reduce stored personal data.

## 🧪 Troubleshooting

* **`ModuleNotFoundError: pymysql`** → `pip install pymysql`
* **MySQL connection refused** → verify host/port/user/pass; ensure MySQL is running.
* **`nltk` resource not found** → run the downloader step again (or set `NLTK_DATA`).
* **TensorFlow errors on CPU** → ensure compatible Python (3.8/3.9 often safest) and install wheels appropriate for your OS/CPU.

## 📜 License

    Apache-2.0

## 🙌 Acknowledgements

Built as part of the **AEC** curriculum. Final result: **A+**.

