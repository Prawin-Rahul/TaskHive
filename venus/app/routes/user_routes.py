import json
from math import ceil

from flask import Blueprint, jsonify, request

from app.models.user import UserProfile
from ..email_utils import send_email
from concurrent.futures import ThreadPoolExecutor

email_thread_pool = ThreadPoolExecutor(max_workers=10)

user_bp = Blueprint("user", __name__)

@user_bp.route("/register", methods=["POST"])
def register_user():
	data = request.get_json()
	try:
		if data :
			user=UserProfile.register_user(data)
			email_thread_pool.submit(
                send_email, 
                subject="Welcome!", 
                recipient=user.email, 
                body="Thanks for signing up!"
            )
			return jsonify(
            {"message": "User registered", "username": user.username}
        ), 201
	except Exception as e:
		return jsonify({"error": str(e)}), 400

@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
	if user_id:
		user=UserProfile.delete_user(user_id=user_id)
	if user:
		return jsonify({"User deleted sucessfully":user.username})
	return jsonify({"error":"NO user found"}),404

@user_bp.route("/<int:user_id>",methods = ["GET"])	
def get_user(user_id):
	user , _tasks = UserProfile.get_user(id=user_id)
	if user:
		return jsonify({
			"id":user.id,
			"username":user.username,
            "email":user.email,
            "bio":user.bio,
			"created_at":user.created_at,
			"tasks":_tasks
		})
	return jsonify({"error": "User not found"}), 404	

@user_bp.route("/",methods=["GET"])
def list_users():
	page = request.args.get("page", 1, type=int)
	per_page = request.args.get("per_page", 5, type=int)
	query = UserProfile.query
	total_users = query.count()
	users = (
		query.offset((page - 1) * per_page).limit(per_page).all()
	) 
	paginated_response = {
			"data": [
				{
					"username": user.username,
					"email": user.email,
					"created_at": user.created_at,
				}
				for user in users
			],
			"pagination": {
				"current_page": page,
				"per_page": per_page,
				"total_pages": ceil(total_users / per_page),
				"total_users": total_users,
			},
		}
	return jsonify(paginated_response), 200

# UPdate user