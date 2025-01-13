from app import db , bcrypt
from datetime import datetime
from sqlalchemy.sql import func
import pytz
from .user import UserProfile
from flask import Blueprint, jsonify, request

class Task(db.Model):
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    # priority = [PO,P1,P2,P3,P4]
    creator_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)  
    # Relationship to users
    steps = db.relationship("Step", backref="task", cascade="all, delete-orphan")
    creator = db.relationship('UserProfile', back_populates='created_tasks')
    # One-to-Many relationship with comments
    comments = db.relationship('Comment', back_populates='task', lazy='dynamic')


    @staticmethod
    def create_task(data):
        new_task = Task(
            title=data["title"],
            description=data["description"],
            creator_id=data["creator_id"]
        )
        db.session.add(new_task)
        db.session.commit()
        return new_task


    @staticmethod
    def get_task(id):
        #TODO: sort step accoring to step_order .
        task = Task.query.filter_by(id=id).first()
        if not task :
            return None , []
        if task:
            _steps = []
            for step in task.steps:
                _steps.append({
                        "step_id":step.id,
                        "description": step.description,
                        "step_order":step.step_order,
                        "created_at":step.created_at,
                        "task_id" : step.task_id,
                })
            return task , _steps
        
    @staticmethod
    def delete_task(id):
        try:
            task = Task.query.filter_by(id=id).first()
            if task:
                db.session.delete(
                    task
                ) 
                db.session.commit()
                return task
            return False
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def update_task():
        pass