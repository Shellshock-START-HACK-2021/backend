from flask import Flask, jsonify
from flask_jwt_extended import (JWTManager, create_access_token, get_jwt,
                                get_jwt_identity, set_access_cookies)
from decouple import config
from datetime import datetime, timedelta, timezone
from flask_cors import CORS

from app import auth, user

app = Flask(__name__)

# Allow COR for whole app
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(auth.bp, url_prefix="/auth")
app.register_blueprint(user.bp, url_prefix="/user")

## JWT settings and init
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config['JWT_SECRET_KEY'] = config("SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=3)
app.config["SECRET_KEY"] = config("SECRET_KEY")
jwt = JWTManager(app)

## JWT refresher
@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response

## Unauthorized request handler
@jwt.unauthorized_loader
def my_invalid_token_callback(expired_token):
    return jsonify(success=False, error="Invalid token or user isn't logged in"), 403

if __name__ == '__main__':
    app.run(debug=True)