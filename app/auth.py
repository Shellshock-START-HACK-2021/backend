from datetime import datetime

import bcrypt
from decouple import config
from flask import Blueprint, jsonify, request
from flask_jwt_extended import (create_access_token, jwt_required,
                                set_access_cookies, unset_jwt_cookies)
from flask_jwt_extended.utils import get_jwt_identity
from pymongo import MongoClient
from werkzeug.security import safe_str_cmp

bp = Blueprint("auth", __name__)
db = MongoClient(f"mongodb+srv://{config('MONGODB_USERNAME')}:{config('MONGODB_PASSWORD')}@{config('MONGODB_HOST')}/?retryWrites=true&w=majority").storemed


@bp.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", False)
    password = request.json.get("password", False)
    if not email:
        return jsonify(success=False, error="No email provided")
    if not password:
        return jsonify(success=False, error="No password provided")

    hashed_password = bcrypt.kdf(password=password.encode("UTF-8"), salt=config("PASSWORD_SALT").encode("UTF-8"), desired_key_bytes=32, rounds=100)
    del password

    user = db.users.find_one({"email": email})
    if user and safe_str_cmp(user["password"], hashed_password):
        access_token = create_access_token(identity=email)
        response = jsonify(success=True)
        set_access_cookies(response, access_token)
        return response
    else:
        return jsonify(success=False, error="Invalid email or password")


@bp.route("/signup", methods=["POST"])
def signup():
    email = request.json.get("email", False)
    password = request.json.get("password", False)
    name = request.json.get("name", False)
    dob = request.json.get("dob", False)
    if not email:
        return jsonify(success=False, error="No email provided"), 400
    if not password:
        return jsonify(success=False, error="No password provided"), 400
    if not name:
        return jsonify(success=False, error="No name provided"), 400
    if not dob:
        return jsonify(success=False, error="No DOB provided"), 400
    if ((datetime.now() - datetime.strptime(dob, '%d-%m-%Y')).days%366) < 18:
        return jsonify(success=False, error="You must be over the age of 18"), 400

    hashed_password = bcrypt.kdf(password=password.encode("UTF-8"), salt=config("PASSWORD_SALT").encode("UTF-8"), desired_key_bytes=32, rounds=100)
    del password
    
    email_check = db.users.find_one({"email": email})
    if not email_check:
        user_schema = {
            "email": email, 
            "password": hashed_password,
            "name": name,
            "dob":datetime.strptime(dob, '%d-%m-%Y')
        }
        insert_user = db.users.insert_one(user_schema)
        if insert_user:
            access_token = create_access_token(identity=email)
            response = jsonify(success=True)
            set_access_cookies(response, access_token)
            return response
        else:
            return jsonify(success=False), 500
    else:
        return jsonify(success=False, error="Email already in use by another account"), 400


@bp.route("/logout", methods=["POST"])
def logout():
    response = jsonify(success=True)
    unset_jwt_cookies(response)
    return response
