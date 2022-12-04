import os
import requests
from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")

def send_simple_message(to, subject, body):
    return requests.post(
		f"https://api.mailgun.net/v3/{DOMAIN}/messages",
		auth=("api", os.getenv("MAILGUN_API_KEY")),
		data={"from": f"Ivan Vrancic <mailgun@{DOMAIN}>",
			"to": [to],
			"subject": subject,
			"text": body})