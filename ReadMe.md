# 🔗 URL Shortener (Django)

A simple and clean URL shortener built with **Django**, **Bootstrap 5**, and **SQLite**.  
Paste a long URL and get a shortened version — quick and easy!

---


https://github.com/user-attachments/assets/41e5b9ff-b52a-4e99-bbfc-a80f7e7e45b1


---

## ⚙️ How It Works

1. The user submits an original URL through the interface.
2. The server hashes the URL using `SHAKE-256` to generate a unique `short_code`.
3. If that short_code already exists in the database (a **hash collision**), the server tweaks the **input to the hash**, **not the original URL**.
4. The original URL is stored in the database along with the new unique short_code.
5. When someone accesses `/short_code/`, they are redirected to the original URL.

---

### 💡 Example of Collision Handling:

```python
import hashlib

def generate_short_code(original_url):
    salt = 0
    short_code = hashlib.shake_256((original_url + str(salt)).encode()).hexdigest(5)

    while UrlData.objects.filter(short_code=short_code).exists():
        salt += 1
        short_code = hashlib.shake_256((original_url + str(salt)).encode()).hexdigest(5)

    return short_code
```

📌 Note: We do not modify the original URL before saving it to the database. Instead, we append a salt only while hashing, ensuring clean data and collision-free short codes.

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
