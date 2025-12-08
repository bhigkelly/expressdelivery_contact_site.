from flask import Flask, render_template, request
from dotenv import load_dotenv
import os, urllib.parse

load_dotenv()

APP_NAME = os.getenv("COMPANY_NAME", "expressdeliveryservice")
CITY = os.getenv("CITY", "Denver, Colorado")
EMAIL = os.getenv("CONTACT_EMAIL", "expressdeliveryservice803@gmail.com")
PHONE = os.getenv("PHONE_DISPLAY", "(630) 287-9378")
WA_NUMBER = os.getenv("WA_NUMBER", "16302879378")  # digits only, e.g., 16302879378

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", app_name=APP_NAME, city=CITY, email=EMAIL, phone=PHONE, wa=WA_NUMBER)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name","").strip()
    subject = request.form.get("subject","").strip() or f"New inquiry - {APP_NAME}"
    message = request.form.get("message","").strip()
    body_lines = [
        f"Inquiry for {APP_NAME}",
        f"Name: {name}",
        f"Subject: {subject}",
        f"Message: {message}"
    ]
    body = "\n".join(body_lines)
    mailto = f"mailto:{EMAIL}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
    wa_text = urllib.parse.quote(f"Hello {APP_NAME} team,\nName: {name}\nSubject: {subject}\nMessage: {message}")
    wa_link = f"https://wa.me/{WA_NUMBER}?text={wa_text}"
    return render_template("thanks.html", app_name=APP_NAME, name=name, subject=subject, message=message, mailto=mailto, wa_link=wa_link, phone=PHONE)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
