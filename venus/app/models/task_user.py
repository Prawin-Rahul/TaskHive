# from app import db

# association table Bridge to link users and tasks.
# two columns: task_id and user_id.
# Each row in this table represents an assignment of a user to a task.

# When a task is assigned to a user, a row is inserted into task_user.
# task_user = db.Table(
#     'task_user',
#     db.Column('task_id', db.Integer, db.ForeignKey('tasks.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('user_profile.id'), primary_key=True)
# )

# db.Table - create association table
#		   - Does not require its own class, as it's not a full model, just a helper table.			
# Columns - task_id: Foreign Key pointing to the id column in the tasks table.
		#   user_id: Foreign Key pointing to the id column in the user_profile table.
	#       Both columns are primary_key to ensure uniqueness (no duplicate assignments).
	
    