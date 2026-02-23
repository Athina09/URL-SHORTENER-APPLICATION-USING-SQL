# Deployment notes – fixing 404 NOT_FOUND

A **404: NOT_FOUND** with an ID like `bom1::tbj8l-...` usually comes from the **host or CDN** (e.g. Cloudflare), not from Django. It means the request never reached your app, or the host couldn’t find a matching route.

## What to check

1. **App is running**  
   On your hosting dashboard, confirm the app is running and that the last deploy succeeded.

2. **Correct URL**  
   Open the **exact app URL** your host gives you (e.g. `https://your-app.onrender.com` or `https://your-app.railway.app`), with no extra path unless you configured one.  
   Don’t use `127.0.0.1` or `localhost` for a deployed app.

3. **Root URL**  
   This app serves the shortener at the **root** (`/`).  
   If the host puts the app under a path (e.g. `/app/`), you must either:
   - Change the host config so the app is at the root, or  
   - Add a URL prefix in Django and use that full URL (e.g. `https://example.com/app/`).

4. **Environment variables (production)**  
   Set on the host:
   - `ALLOWED_HOSTS`: your app’s hostname(s), comma-separated (e.g. `your-app.onrender.com`).
   - `DJANGO_SECRET_KEY`: a long random string (and keep it secret).
   - Optional: `DJANGO_DEBUG=False` for production.

5. **Build and start command**  
   - **Build:** `pip install -r requirements.txt` (and run from repo root so `urlshortener/` is present).  
   - **Start:** use the Procfile: `cd urlshortener && gunicorn urlshortener.wsgi:application --bind 0.0.0.0:$PORT`  
   If the host runs from inside `urlshortener/`, use: `gunicorn urlshortener.wsgi:application --bind 0.0.0.0:$PORT`.

## Run locally

```bash
cd /Users/apple/Lab-2
source myenv/bin/activate
cd urlshortener
python manage.py runserver
```

Then open **http://127.0.0.1:8000/** (only for local use).
