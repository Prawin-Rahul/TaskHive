# TaskHive

## Project Overview

TaskHive is a task management platform . This project focuses on backend architecture, interactions, and applying essential concepts such as database schema design, Hashing Passwd, routing, authentication(JWT), authorization, and notifivation system.

---

## Features

### Core Features

- **User Profiles**:
  - Create, view, edit, and delete user profiles.
- **Tasks **:
  - Create, view, update, delete .
- **Steps **:
  - Create, update, delete .
- **Comments **:
  - Create, update, delete .
- **Pagination**:
  - Efficiently load feed data with limited items per request.

---

## Tech Stack

### Backend

- **Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Notification**: Gmail API

### Tools and Libraries

- **Environment Management**: virtualenv

---

## Installation and Setup

### Prerequisites

Ensure the following are installed on your system:

- Python 3.8+
- SQLite
- Flask

### Steps to Run

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/TaskHive.git
   cd TaskHive
   ```

2. **Set Up Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file with the following:

   ```env
   SECRET_KEY=your_secret_key
   ```

5. **Run Database Migrations**:

   ```bash
   flask db upgrade
   ```

6. **Start the Application**:

   ```bash
   python mars/run.py
   ```

---

## Project Structure

```
Desktop/TaskHive/venus/
├── app/                  # Core application logic
│   ├── __init__.py       # App initialization and factory
│   ├── models/
│   │   ├── __init__.py   # Models initialization
│   │   ├── user.py
│   │   ├── task.py
|   |   |__ comment.py
|   |   |__ step.py
|   |   |__ step_user.py
│   ├── routes/
│   │   ├── __init__.py   # Routes initialization
│   │   ├── user_routes.py
│   │   ├── task_routes.py
│   │── email_utils.py
├── __init__.py
├── Pipfile               # Pipenv dependency management
├── Pipfile.lock          # Locked dependencies
├── README.md             # Project documentation
├── Learnings.md             # Learnings documentation
├── run.py                # Application entry point
├── .env                  # Environment variables
├── .gitignore            # Ignored files and folders
```

---

## API Endpoints

### Authentication

- **POST** `/users/register`: Register a new user.
- **POST** `/users/login`: Login a user.

### User Profiles

- **GET** `/users/<id>`: Retrieve a Specific user profile.
- **PUT** `/users/<id>`: Update a user profile.
- **DELETE** `/users/<id>`: Delete a user profile.
- **GET** `/users/`: Retrieve all Users (Organisation level)

### Tasks

- **GET** `/tasks/<int:task_id>`: Retrieve all tasks (paginated)-For specific user
- **POST** `/tasks`: Create a new task.
- **GET** `/tasks/<id>`: Retrieve a specific task.
- **PUT** `/tasks/<id>`: Update a task.
- **DELETE** `/tasks/<id>`: Delete a task.

### Steps

- **POST** `/tasks/<int:task_id>/step`: Create a step
- **UPDATE** `/tasks/<int:task_id>/steps/<int:step_id>` : Update a task
- **DELETE** `/tasks/<int:task_id>/steps/<int:step_id>` : Delete a task

### Comment

- **POST** `/tasks/<int:task_id>/comment`: Post a comment.
- **DELETE** `tasks/<int:task_id>/comments/<int:comment_id>`: Delete a comment.
- **UPDATE** `/tasks/<int:task_id>/comments/<int:comment_id>`: Update a comment.

---

## Schema

### user profile schema

```
Column Name	Data Type		Description
id			Integer (PK)	Unique identifier for the task.
title		String			Title of the task.
assigned_to	Many-to-Many	Link to users assigned to this task.
due_on		DateTime		Deadline for the task.
created_at	DateTime		Timestamp for when the task was created.
updated_at	DateTime		Timestamp for the last update.
```

### task schema

```
Column Name		Data Type		Description
id				Integer (PK)	Unique identifier for the step.
creator_id		Integer (FK)	Links the task to a specific user.
title           string          Title of the task
description		String			Details about the step.
assigned_to		Integer (FK)	Links the step to a user.
is_completed	Boolean	Whether the step is completed.
created_at		DateTime		Timestamp for when the step was created.
updated_at		DateTime		Timestamp for the last update.
due_date		DateTime		Deadline for task
```

### step schema

```
Column Name	Data Type		Description
id			Integer (PK)	Unique identifier for the comment.
task_id		Integer (FK)	Links the comment to a specific task.
content		Text			The text of the comment.
created_at	DateTime		Timestamp for when the comment was created.
updated_at	DateTime		Timestamp for when the comment was updated.
completed   Boolean         If step if completed or Not
assigned_users              Association table - users involved in step
```

### comment schema

```
Column Name	Data Type		Description
id			Integer (PK)	Unique identifier for the comment.
task_id		Integer (FK)	Links the comment to a specific task.
user_id		Integer (FK)	Links the comment to the user who made it.
content		Text			The text of the comment.
created_at	DateTime		Timestamp for when the comment was created.
```

---

## Future Enhancements

- Implement Celery and Redis as Task queue and Message broker for better handling of concurrency and decoupling notification system for main application logic.
- Enhance security features (OAuth, 2FA).
- Rate limiters
- API versioning
- Optimize database performance with indexing.
- Keep proity at task level - notify upon deadline . sort task based on priority upon retrivel.
- Handle failed Emails
- If Will database look , If application is used by many organisation (Should I add a new column)

## Contribution

Feel free to fork this repository and submit pull requests. For major changes, open an issue first to discuss what you would like to change.

---

## Contact

For any questions or feedback, please reach out at [prawinrahul1411@gmail.com].
'

## simple pending tasks
1. Add JWT
2. Add Authorization
3. Data Validation
