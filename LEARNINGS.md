# Learning Documentation

---

## Project Overview

This project is built using

1. Flask and SQLAlchemy
2. leveraging REST architecture
3. JWT for authentication
4. Bcrypt for password hashing
5. Gmail API for Sending Notifications
6. Thread pool to handle concurrency of Blcking function

---

I Started this project , Thinking to build a application like BaseCamp (Basically a Extenstion of todo) , with notification system to manage and keep track of Projects tasks for an Organisation .


## Key Learnings & Concepts

### 1. Gmail API for Notification

Initally I planed for using Flask_mail library to send notification via Gmail .
The References I checked , we suggesting to use Username(email) and password method to acess Gmail functions .
But As of Jan1 2025 , The username-passwd method was no longer avalible due to security reason .
So had to establish connection to Gmail using Oauth credentials .
It was a great Learning to understand about the Establishing Scope for the Gmail functions(I Choose only send) .

```python

import base64
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import os

# Function to send email using Gmail API
def send_email(subject, recipient, body):
    try:
        creds = get_credentials()
        service = build("gmail", "v1", credentials=creds)

        # Create the email content
        message = MIMEText(body)
        message["to"] = recipient
        message["subject"] = subject

        # Encode the message to Base64
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

```

### 2. Blocking Functions

As the sending Email was taking 3-5 sec , Hence blocking the flow of program . I thought of making it Asynchronous .
I though Once I manage to put the mail_send() task to Event loop , I can be
But Gmail API turned out to be a Synchronous, Hence a Blocking Function . So had to create a Thread to keep this Blocking function out of Event loop . So that the main server , can focus on User requests .

```python
import json
from math import ceil

from flask import Blueprint, jsonify, request

from app.models.user import UserProfile
from ..email_utils import send_email
from concurrent.futures import ThreadPoolExecutor

email_thread_pool = ThreadPoolExecutor(max_workers=10)

user_bp = Blueprint("user", __name__)

@user_bp.route("/register", methods=["POST"])
def register_user():
	data = request.get_json()
	try:
		if data :
			user=UserProfile.register_user(data)
			email_thread_pool.submit(
                send_email,
                subject="Welcome!",
                recipient=user.email,
                body="Thanks for signing up!"
            )
			return jsonify(
            {"message": "User registered", "username": user.username}
        ), 201
	except Exception as e:
		return jsonify({"error": str(e)}), 400
```

### 3. Thread pool

Question : As Email sending , was expecting creation of threads .
So If 100 user registration happens Simultaneously - 100 threads are created - This would lead to resource exhaustion of the system .

1. TO handle I had to control the concurrency of email sending tasks .
2. One of the suggestion was using celery (Task queue system) , Thread-pool, etc ..
3. By the requirement of the project , I choose Thread-pool .

```python
from concurrent.futures import ThreadPoolExecutor

email_thread_pool = ThreadPoolExecutor(max_workers=10)
```

### 4. Real world Domain perspective

The Email send as notification has To Adress as "prawinrahul1411@gmail.com".
``` python
From:  Prawinrahul@gmail.com
To: recipient@example.com
Date: 4 Jan 2025, 06:33x
Subject: Taskhive: Task Completed
Mailed-By: gmail.com
Signed By: gmail.com
Security: Standard encryption (TLS)
```
But I had a plan to make it "notifications@taskhive.com" .

```python
from:	Basecamp (Org name) <notifications@taskhive.com>
to:	prawin@org.app
date:	4 Jan 2025, 06:33
subject:	Basecamp (orgName): Here’s the latest activity
mailed-by:	taskhive.com
Signed by:	taskhive.com
security:	 Standard encryption (TLS)

```
I Did some few research, which gave mr the understading of :

1. Register a Domain
2. Set Up Email Hosting
3. Configure DNS Settings
4. Integrate with Your App

Though I didnot do any of the Above , lioke purhasing domain . But Gave a good Idea of How Taskhive as a organisation can configure their Email servise , how other other company can leverege this service etc ..

---
### Todo

Now am Curoius of How the Ntification service will work at scale .
1. How to implement celery , redis , Distibution system etc ..
2. Email notification is send to user .if assigned to a step in a task , a comment in made on a task , in which user is Involved etc .
This might be anoying . How to club the notification received in a specific time Interval .
etc ..