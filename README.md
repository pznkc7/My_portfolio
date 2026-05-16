# 🧑‍💻 Puzan Kc — Personal Portfolio

A personal portfolio website built with **Python** and **Django**, featuring a contact system, certificate showcase, music player, and curated developer tools — all served through a clean, dark-themed UI.

---

## 🌐 Live Demo

> _Not hosted yet — run locally using the steps below._

---

## 📸 Screenshots

>(coming soon)

---

## 🛠️ Tech Stack

| Layer      | Technology                        |
|------------|-----------------------------------|
| Backend    | Python 3.x, Django 5.2            |
| Database   | SQLite (development)              |
| Frontend   | HTML, CSS, Bootstrap 5, JavaScript|
| Email      | Gmail SMTP via Django EmailMessage |
| Media      | Django FileField / ImageField     |
| Auth       | Django Admin                      |

---

## ✨ Features

- **Home page** — Hero section with profile, skills, and stats
- **About page** — Bio, animated skill bars, and approach to development
- **Contact form** — Saves message to database and sends a thank-you email to the visitor automatically
- **Certificates page** — Admin uploads certificates with image, title, organization, and date; displayed as cards
- **Music Player** — SoundCloud-style player with play/pause, seek bar, skip, shuffle, and repeat — songs managed via Django admin
- **Movie Guide** — Curated movie recommendations by genre
- **Useful Sites** — Handpicked developer resources and tools
- **Django Admin** — Full admin panel to manage contacts, certificates, and songs

---

## 📁 Project Structure

```
MY_PORTFOLIO/                       ← Root project folder
│
├── port_env/                       ← Virtual environment (not committed)
│
├── portweb/                        ← Main Django project folder
│   │
│   ├── media/                      ← Uploaded files (certificates, music)
│   │   ├── certificate/            ← Certificate images
│   │   └── music/                  ← Uploaded .mp3 files
│   │
│   ├── portapp/                    ← Main Django app
│   │   ├── __pycache__/
│   │   ├── migrations/             ← Database migrations
│   │   ├── static/
│   │   │   └── images/             ← Profile and static images
│   │   ├── templates/
│   │   │   └── portapp/
│   │   │       ├── base.html       ← Navbar + footer base layout
│   │   │       ├── home.html
│   │   │       ├── about.html
│   │   │       ├── contact.html
│   │   │       ├── certificate.html
│   │   │       ├── music.html
│   │   │       ├── tools.html
│   │   │       ├── movieguide.html
│   │   │       ├── sites.html
│   │   │       └── msg.html        ← Auto-reply email template
│   │   ├── __init__.py
│   │   ├── admin.py                ← Admin panel registrations
│   │   ├── apps.py
│   │   ├── models.py               ← Contact, Certificate, Song models
│   │   ├── tests.py
│   │   └── views.py                ← All page views
│   │
│   ├── portweb/                    ← Django project config
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py             ← Project settings
│   │   ├── urls.py                 ← URL routing
│   │   └── wsgi.py
│   │
│   ├── .env                        ← Secret keys (never committed)
│   ├── .gitignore
│   ├── db.sqlite3                  ← SQLite database (not committed)
│   ├── manage.py
│   ├── README.md
│   └── requirements.txt
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/pznkc7/My_portfolio
cd My_portfolio
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the root directory

```env
SECRET_KEY=your-django-secret-key-here
DEBUG=True
EMAIL_HOST_PASSWORD=your-gmail-app-password-here
```

> **Note:** For Gmail, use an **App Password** — not your regular Gmail password.
> Generate one at: Google Account → Security → 2-Step Verification → App Passwords

### 5. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (for Django admin)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 🔑 Admin Panel

Go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

From the admin panel you can:
- View and manage **contact form submissions**
- Add, edit, or delete **certificates** (with image upload)
- Add, edit, or delete **songs** for the music player (upload `.mp3` files)

---

## 📦 Dependencies

Generate your `requirements.txt` with:

```bash
pip freeze > requirements.txt
```

Key packages used:

```
Django==5.2
Pillow          # For ImageField (certificate images)
python-decouple # For .env environment variables
```

---

## 🔒 Environment Variables

| Variable            | Description                          |
|---------------------|--------------------------------------|
| `SECRET_KEY`        | Django secret key                    |
| `DEBUG`             | `True` for development, `False` for production |
| `EMAIL_HOST_PASSWORD` | Gmail App Password for sending emails |

---

## 📬 Contact Form Flow

1. Visitor fills out name, email, subject, message
2. Data is saved to the `Contact` model in the database
3. A thank-you email is automatically sent to the visitor's email address
4. You can view all submissions in the Django admin panel

---

## 🎵 Music Player

- Admin uploads `.mp3` files via Django admin → Songs section
- Files are stored in `media/music/`
- Player supports: **play/pause**, **seek bar**, **skip prev/next**, **shuffle**, **repeat**
- Waveform visualization updates in real time as the song plays

---

## 🚀 Deployment (Coming Soon)

Planned deployment on **Railway** or **Render** with:
- PostgreSQL database
- Environment variables configured via platform dashboard
- Static files served via WhiteNoise
- Media files via Cloudinary

---

## 👨‍💻 Author

**Puzan Kc**
- GitHub: [@pznkc7](https://github.com/pznkc7)
- LinkedIn: [pujan-khatri](https://www.linkedin.com/in/pujan-khatri-960b88386/)
- Email: khatripujan35@gmail.com

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).