# 🔗 URL Shortener (Django)

A simple and clean URL shortener built with **Django**, **Bootstrap 5**, and **SQLite**.  
Paste a long URL and get a shortened version — quick and easy!

---


https://github.com/user-attachments/assets/41e5b9ff-b52a-4e99-bbfc-a80f7e7e45b1


---
## 🚀 Features

- Shortens long URLs
- Auto-generates unique short codes
- Redirects to original URLs via short links
- Copy short URL to clipboard with one click
- Responsive UI using Bootstrap 5 (Dark theme)

---
## 🖥️ Tech Stack

- Backend: Django (Python)
- Frontend: HTML, Bootstrap 5
- Database: SQLite (default)

```
---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

> ✨ If `requirements.txt` not yet added, create one:

```bash
pip freeze > requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Start the Server

```bash
python manage.py runserver
```

Visit 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## ✍️ Usage

- Paste a long URL in the input field.
- Click **Shorten**.
- Copy the generated short link and share it.
- Visiting the short link will redirect to the original URL.

---

## 🛠️ Example Model (models.py)

```python
from django.db import models


class UrlData(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
```
