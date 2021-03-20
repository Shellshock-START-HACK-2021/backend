from decouple import config
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from flask_jwt_extended.utils import get_jwt_identity
from pymongo import MongoClient

bp = Blueprint("user", __name__)
db = MongoClient(f"mongodb+srv://{config('MONGODB_USERNAME')}:{config('MONGODB_PASSWORD')}@{config('MONGODB_HOST')}/?retryWrites=true&w=majority").storemed

@bp.route("/history")
@jwt_required()
def get_user_history():
    email = get_jwt_identity()
    user = db.users.find_one({"email": email})
    if not user:
        return jsonify(success=False, error="Unable to find user"), 400
    history = user["history"]
    return jsonify(success=True, history=history), 200

@bp.route("/account/info", methods=["GET", "POST"])
@jwt_required()
def get_account_inof():
    email = get_jwt_identity()
    if request.method == "GET":
        user = db.users.find_one({"email": email}, {"history": 0, "_id":0, "password": 0})
        if not user:
            return jsonify(success=False, error="Unable to find user"), 400
        return jsonify(success=True, user_info=user), 200
    else:
        user_modify = db.users.update_one({"email": email}, {"$set": request.json})
        if user_modify:
            return jsonify(success=True), 200
        else:
            return jsonify(success=False), 500