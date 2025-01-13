from app import db , bcrypt
from datetime import datetime
from sqlalchemy.sql import func
import pytz

class UserProfile(db.Model):
    
    __tablename__ = 'user_profile'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    bio = db.Column(db.String, nullable=True)
    image = db.Column(db.String, nullable=True)
    password = db.Column(db.String(100))
    # Assosiation table
    assigned_steps = db.relationship(
        'Step',
        secondary ='step_user',
        back_populates='assigned_users'
    )
    created_tasks = db.relationship('Task', back_populates='creator', lazy='dynamic')
    # # One-to-Many relationship with comments
    comments = db.relationship('Comment', back_populates='commenter', lazy='dynamic')

    def set_password(self, raw_password):
        self.password = bcrypt.generate_password_hash(raw_password).decode("utf-8")

    def check_password(self, raw_password):
        return bcrypt.check_password_hash(self.password, raw_password)

	# Method to get IST time		
    def get_created_at_ist(self):	
        ist = pytz.timezone("Asia/Kolkata")
        return self.created_at.astimezone(ist) if self.created_at else None

    # CRUD Ops
    @staticmethod
    def register_user(data):
        if not all(
            key in data
            for key in ["username", "email", "password",]
        ):
            raise ValueError("Missing required fields")
        if UserProfile.query.filter_by(email=data["email"]).first():
            raise ValueError("Email already exists")

        user = UserProfile(
            username = data["username"],
            email = data["email"],
            bio = data["bio"] or "",
        )
        # hash the password
        user.set_password(data["password"])
        db.session.add(user)
        db.session.commit()
        
        return user
    
    @staticmethod
    def delete_user(user_id):
        try:
            user = UserProfile.query.filter_by(id=user_id).first()
            print(user)
            if user:
                db.session.delete(
                    user
                ) 
                db.session.commit()
                return user

            return False
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_user(id):
        user = UserProfile.query.filter_by(id=id).first()
        _tasks = []
        if not user:
            return None, []
        if user:
            for task in user.created_tasks:
                    _tasks.append({
                        "task_id":task.id,
                        "title": task.title,
                        "description": task.description,
                        "created_at":task.created_at,
                    })
            
        return user , _tasks

    @staticmethod
    def list_users():
        _users= []
        users = UserProfile.query.all()
        for user in users:
            _users.append({
            "username":user.username,
            "email":user.email,
            "bio":user.bio,
            "user_id":user.id,
        })
        return _users

    @staticmethod
    def update_user(updates,id):
        pass
