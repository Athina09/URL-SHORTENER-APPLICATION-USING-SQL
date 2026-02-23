# Expt.No: 2 – URL Shortener Application Using SQL

**Aim:** Build a URL shortener using SQL and Django.

## Project Structure

```
Lab-2/
├── myenv/                 # Virtual environment
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── urlshortener/          # Django project
    ├── manage.py
    ├── db.sqlite3         # Created after migrate
    └── urlshortener/      # Project settings
    │   ├── settings.py
    │   └── urls.py
    └── urlshort/          # URL shortener app
        ├── models.py      # URL, UrlModel
        ├── views.py       # home, shorten_url, redirect_to_original
        ├── urls.py
        ├── utils.py       # generate_short_url (base alphanumeric)
        ├── forms.py       # ShortenURLForm
        ├── admin.py
        └── templates/urlshort/
            ├── home.html
            ├── shorten_url.html
            └── redirect.html
```

## Execution Steps

### 1. Virtual environment (already created)

```bash
python3 -m venv myenv
source myenv/bin/activate   # Windows: myenv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install Django
# or: pip install -r requirements.txt
```

### 3. Apply migrations (if not done)

```bash
cd urlshortener
python manage.py makemigrations
python manage.py migrate
```

### 4. Create superuser (optional, for admin)

```bash
python manage.py createsuperuser
```

### 5. Run development server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in a browser.

## Usage

- **Home:** List of stored URLs and a form to shorten a new URL.
- **Shorten:** Submit a long URL; it is stored and a 6-character short code is generated (alphanumeric).
- **Redirect:** Visiting `http://127.0.0.1:8000/<short_url>/` redirects to the original URL.

## Database

- **Engine:** SQLite (`db.sqlite3` in project root).
- **Models:** `URL` (long_url, short_url), `UrlModel` (user, original_url, short_url for future use).

## Outputs

- Home page shows “Welcome to the URL Shortener”, list of stored URLs, and the shorten form.
- After shortening, you are redirected to home and see the new short link.
- Clicking a short link redirects to the original URL.
