# customer360 — deployment notes

This repository contains a minimal Django app `customer360` (local development supported).

Important: GitHub Pages only serves static sites (HTML/CSS/JS). It cannot host a Django app (server-side Python). Use one of the recommended deployment platforms below for a full Django deployment.

Recommended quick deployments

- Render (recommended): free and easy GitHub integration for Django. Use `Procfile` + `requirements.txt` and Render will auto-deploy from a connected GitHub repo.
- Railway, Fly.io, or Vercel (Vercel needs a container/Docker setup for Django).
- Use Docker and GitHub Actions to deploy to any cloud provider.

Quick push to GitHub (run locally):

```bash
# from project root
git add --all
git commit -m "Prepare for deployment: Procfile, requirements, gitignore"
# add remote if not already set (replace <your-repo-url>)
git remote add origin <your-repo-url>
git push -u origin main
```

Deploy to Render (example)

1. Create a free account at https://render.com and connect your GitHub account.
2. Create a new Web Service and pick this repository.
3. Set the Environment to `Python 3.x` (choose a 3.11/3.12/3.13 runtime supported by Render), Start Command: `gunicorn customer360.wsgi:application --log-file -` (the `Procfile` also helps), and the Build Command: `pip install -r requirements.txt`.
4. Set any needed environment variables in Render (e.g., `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`), and then deploy.

Static files

This app uses Django's `staticfiles`. In production configure `whitenoise` or an external storage (S3) and run `collectstatic` during the build. Example build step:

```bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
```

If you want, I can:
- Create a GitHub Action workflow to build and deploy (Docker or to a provider that supports Actions).
- Prepare a Dockerfile and GitHub Actions to build & deploy the container.
