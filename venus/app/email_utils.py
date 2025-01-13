import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import os

# Path to the token.json file
TOKEN_PATH = "/home/prawin/Desktop/TaskHive/venus/token.json"

# Load credentials
def get_credentials():
    creds = Credentials.from_authorized_user_file(TOKEN_PATH, scopes=["https://www.googleapis.com/auth/gmail.send"])
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())
    return creds

def send_email(subject, recipient, body):
    try:
        creds = get_credentials()
        service = build("gmail", "v1", credentials=creds)

        # Create the email content
        message = MIMEText(body)
        message["to"] = recipient
        message["subject"] = subject

        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")

        # Send the email
        message = (
            service.users()
            .messages()
            .send(userId="me", body={"raw": raw_message})
            .execute()
        )
        print(f"Email successfully sent to {recipient}")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {str(e)}")
        raise
