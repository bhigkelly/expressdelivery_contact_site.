# expressdeliveryservice — Contact-only Site (Flask)
Minimal website where customers can contact management via WhatsApp, Email, or Phone.

## Run on Windows
```bat
py -m venv .venv
.\.venv\Scriptsctivate
pip install flask python-dotenv
py app.py
```
Open http://127.0.0.1:5000

## Configure (optional)
Create `.env` with:
```
COMPANY_NAME=expressdeliveryservice
CITY=Denver, Colorado
CONTACT_EMAIL=expressdeliveryservice803@gmail.com
PHONE_DISPLAY=(630) 287-9378
WA_NUMBER=16302879378
```
