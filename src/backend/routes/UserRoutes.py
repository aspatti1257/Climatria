from flask import Blueprint, request, jsonify
from src.database.UserDAO import UserDAO
from src.database.CredentialParser import CredentialParser
from src.LoggerFactory import LoggerFactory
from src.backend.User import User

# Initialize the blueprint
user_blueprint = Blueprint('user', __name__)

# Set up the logger
log = LoggerFactory.create_log(__name__)


@user_blueprint.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    if not data:
        log.warning("No data provided in the signup request.")
        return jsonify({"error": "No data provided."}), 400
    
    try:
        # Create a User object from the received data
        user = User(
            email=data.get('email'),
            name=data.get('name'),
            phone_number=data.get('phone_number'),
            ba=data.get('balancingAuthority'),
            zip_code=data.get('zipCode'),
            last_alert=None
        )
        parser = CredentialParser("../../credentials.txt")
        creds = parser.fetch_credentials()
        # Interact with the database using UserDAO
        user_dao = UserDAO(creds[0], creds[1])
        user_dao.create(user)
        log.info(f"User {user.get_id()} signed up successfully")

        return jsonify({"message": "User signed up successfully"}), 201
    
    except Exception as e:
        log.error(f"Error during signup: {str(e)}")
        return jsonify({"error": "An error occurred during signup"}), 500
