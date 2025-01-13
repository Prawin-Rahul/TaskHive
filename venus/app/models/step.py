from app import db , bcrypt
from datetime import datetime
from sqlalchemy.sql import func
import pytz
from .user import UserProfile
from .step_user import step_user
from flask import Blueprint, jsonify, request



class Step(db.Model):
    __tablename__ = 'steps'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_id = db.Column(db.Integer, db.ForeignKey("tasks.id"), nullable=False)  # Links step to a task
    description = db.Column(db.Text, nullable=False)
    step_order = db.Column(db.Integer, nullable=False)  # Order of the step in the task
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    completed = db.Column(db.Boolean,default=False)
    # Relationship to users
    assigned_users = db.relationship(
        'UserProfile',
        secondary='step_user',  # Association table name 
        back_populates='assigned_steps'
    )
    
    @staticmethod
    def create_step(task_id,data):
        for step in data :
            if not step.get("description") or not step.get("step_order"):
                raise ValueError("Step description and order are required")
            new_step = Step(
                task_id=task_id,
                description=step["description"],
                step_order = step["step_order"]
            )
            if "user_ids" in data:
                user_ids = data["user_ids"]
                # The "in_" clause in the query filters all users with id values in that array.
                users = UserProfile.query.filter(UserProfile.id.in_(user_ids)).all()
                if len(users) != len(user_ids):
                    return jsonify({"error": "Some user IDs are invalid"}), 400
                new_step.assigned_users = users
            db.session.add(new_step)
            db.session.commit()
    
    @staticmethod
    def delete_step(id):
        try:
            step = Step.query.filter_by(id=id).first()
            if step:
                db.session.delete(
                    step
                ) 
                db.session.commit()
                return step

            return False
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_step(id):
        pass    