# An association table, step_user, will allow many-to-many relationships between steps and users.
from app import db

step_user = db.Table(
    'step_user',
    db.Column('step_id', db.Integer, db.ForeignKey('steps.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user_profile.id'), primary_key=True)
)