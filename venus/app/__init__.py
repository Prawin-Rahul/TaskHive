## Flask application factory:

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
import os
from dotenv import load_dotenv
import logging

load_dotenv()

# GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')

db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()

def create_app():
    app = Flask(__name__)  
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project2.db"
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USERNAME'] = 'prawinrahul1411@gmail.com'
    # app.config['MAIL_PASSWORD'] = GMAIL_PASSWORD 
    app.config['MAIL_DEBUG'] = True
    db.init_app(app)
    bcrypt.init_app(app) 
    mail.init_app(app)

    
    from app.routes.user_routes import user_bp
    from app.routes.tasks_routes import task_bp

    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(task_bp, url_prefix="/api/tasks")

    return app 