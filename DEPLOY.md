
# Deploy this site (Render.com)

## 1) Make a GitHub repo
- Go to github.com → New repository → **expressdelivery_contact_site** (public is fine).
- On your PC, open the folder and upload all files (drag & drop on GitHub).

## 2) Create a Render Web Service
- Go to render.com → New → **Web Service** → Connect your GitHub repo.
- Environment: **Python**
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Add these environment variables (if not using `render.yaml`):
  - COMPANY_NAME=expressdeliveryservice
  - CITY=Denver, Colorado
  - CONTACT_EMAIL=expressdeliveryservice803@gmail.com
  - PHONE_DISPLAY=(630) 287-9378
  - WA_NUMBER=16302879378

## 3) Wait for deploy, then open the URL
- Example: https://expressdeliveryservice.onrender.com (your URL may differ).
- Test the form → WhatsApp / Email buttons.

## 4) (Optional) Add your domain
- In Render service → Settings → Custom Domains → Add domain.
- Follow the DNS instructions (CNAME for www, A records for root) from Render.
