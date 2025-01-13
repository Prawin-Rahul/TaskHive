from app import db

class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=False)
    # created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    # updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Foreign key linking the comment to the user who created it
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    # Foreign key linking the comment to the task
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)

    # Relationship back to UserProfile (commenter)
    commenter = db.relationship('UserProfile', back_populates='comments')
    # Relationship back to Task
    task = db.relationship('Task', back_populates='comments')

    @staticmethod
    def create_comment(task_id,data):
        new_comment = Comment(
            description=data["description"],
            user_id=data["user_id"],
            task_id=task_id
        )
        db.session.add(new_comment)
        db.session.commit()
        return new_comment
