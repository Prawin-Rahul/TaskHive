from tasks_routes import task_bp
from flask import request , jsonify
from app.models.step import Step

# @task_bp.route("/<task_id>/steps", methods=["POST"])  
# def user_operation():
#     if request.method == "POST":
#         return create_step()

# @task_bp.route("/<int:task_id>/steps", methods=["POST"])  
# def create_step(task_id):
#     data = request.get_json()
#     print(data)
#     try:
#         new_step = Step.create_step(task_id=task_id,data=data)
#         return jsonify({"message": "Step created", "userid": new_step.id}), 201
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400


# POST /api/tasks/<task_id>/steps - Add a step to a task.
# GET /api/tasks/<task_id>/steps - Get all steps for a task.
# PUT /api/tasks/<task_id>/steps/<step_id> - Update a step for a task.
# DELETE /api/tasks/<task_id>/steps/<step_id> - Delete a step from a task.