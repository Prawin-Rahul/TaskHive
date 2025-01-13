from flask import Blueprint, jsonify, request
import json
from math import ceil

from app.models.task import Task  
from app.models.step import Step
from app.models.comment import Comment
from ..email_utils import send_email

task_bp = Blueprint("posts", __name__)
  
@task_bp.route("/", methods=["GET", "POST"])  
def user_operation():
    if request.method == "POST":
        return create_task()
   
@task_bp.route("/<int:task_id>/steps", methods=["POST"])  
def create_step(task_id):
    data = request.get_json()
    print(data)
    try:
        # Notify user via Email - if user is included in step
        Step.create_step(task_id=task_id,data=data)
        return jsonify({"message": "Step created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
      
@task_bp.route("/step/<int:step_id>", methods=["DELETE"])
def delete_step(step_id):
	if step_id:
		step=Step.delete_step(id=step_id)
	if step:
		return jsonify({"Step deleted sucessfully":step.description})
	return jsonify({"error":"NO Step found"}),404


@task_bp.route("/<int:task_id>/comment", methods=["POST"])  
def create_comment(task_id):
    data = request.get_json()
    print(data)
    try:
        new_comment = Comment.create_comment(task_id=task_id,data=data)
        return jsonify({"message": "Comment created", "userid": new_comment.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

def delete_comment(comment_id):
      pass

def update_comment(task_id):
      pass

def create_task():
    data = request.get_json()
    try:
        new_post = Task.create_task(data)
        return jsonify({"message": "Task created", "userid": new_post.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@task_bp.route("/<int:task_id>",methods = ["GET"])	
def get_task(task_id):
	task , _steps = Task.get_task(id=task_id)
	if task:
		return jsonify({
			"id":task.id,
			"title":task.title,
            "description":task.description,
			"created_at":task.created_at,
			"steps":_steps
		})
	return jsonify({"error": "User not found"}), 404	

@task_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
	if task_id:
		task=Task.delete_task(id=task_id)
	if task:
		return jsonify({"Task deleted sucessfully":task.title})
	return jsonify({"error":"NO task found"}),404


# read :task user sperfic 
#      : priority specific 
# update : 1 task , per time


# steps : READ :user specidic , under task key 
#               cannot rad task seperately
#              : Due Date
#       : update :  1 step , per time

 
#STeps
# Add - api/tasks/<int:task_id>/steps"
# Delete - api/tasks/<int:task_id>/steps/<int:step_id>
# Read - No need to read step seperately - Just as apart of Task
# Update - api/tasks/<int:task_id>/steps/<int:step_id> - complete , change desp
# Add steps in bulk , for a task 

# Tasks
# Add - api/tasks/"
# Delete - api/tasks/<int:task_id>/
# Read - One task  - api/tasks/<int:task_id>/
# Read - all/many task  - AS ap part of user Profile
# Update - api/tasks/<int:task_id>/ - complete , change desp , title

# Comments
# Add - api/tasks/<int:task_id>/comment/"
# Delete - api/tasks/<int:task_id>/comment/<int:comment_id>
# Read - No need to read step seperately - Just as apart of Task
# Update - api/tasks/<int:task_id>/comment/<int:comment_id>-  change desp
    
# To add steps in bulk, the payload could be an array of step objects. 
# The endpoint remains the same, and your logic should handle batch inserts.
# Always Add step in array - one or More
# Array of steps - loop array - add step one after other 