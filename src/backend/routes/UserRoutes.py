from flask import Blueprint, request, jsonify
from src.database.UserDAO import UserDAO
from src.LoggerFactory import LoggerFactory
from src.backend.User import User
from src.backend.SinchTrigger import SinchTrigger

# Initialize the blueprint
user_blueprint = Blueprint('user', __name__)

# Set up the logger
log = LoggerFactory.create_log(__name__)

# Interact with the database using UserDAO
user_dao = UserDAO()

# Set up the messaging service for verification
sinch = SinchTrigger()


@user_blueprint.route('/api/start_verification', methods=['POST'])
def start_verification():
    data = request.json
    if not data:
        log.warning("No data provided in the signup request.")
        return jsonify({"error": "No data provided."}), 400
    try:
        phone_number = data.get("phoneNumber")
        verification_result = sinch.attempt_verify(phone_number)
        # TODO: In memory cache would avoid the need to send this to the client.
        return jsonify({'verificationId': verification_result.id}), 200
    except Exception as e:
        log.error(e)


@user_blueprint.route('/api/report_code', methods=['POST'])
def finalize_verification():
    data = request.json
    if not data:
        log.warning("No verification code in the signup request.")
        return jsonify({"error": "No data provided."}), 400
    try:
        code = data.get("code")
        verification_id = data.get("verificationId")
        response = sinch.report_code(verification_id, code)
        return jsonify({'verificationResponse': response}), 200
    except Exception as e:
        log.error(e)


@user_blueprint.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    if not data:
        log.warning("No data provided in the signup request.")
        return jsonify({"error": "No data provided."}), 400
    
    # Check if the email already exists
    email = data.get("email")
    existing_user = user_dao.find_by_id(email)
    if existing_user:
        return jsonify({"error": "Email already exists"}), 409
    
    try:
        # Create a User object from the received data
        user = User(
            email=data.get('email'),
            name=data.get('name'),
            phone_number=data.get('phoneNumber'),
            ba=data.get('balancingAuthority'),
            zip_code=data.get('zipCode'),
            last_alert=None
        )

        user_dao.create(user)
        log.info(f"User {user.get_id()} signed up successfully")

        return jsonify({"message": "User signed up successfully"}), 201
    
    except Exception as e:
        log.error(f"Error during signup: {str(e)}")
        return jsonify({"error": "An error occurred during signup"}), 500


@user_blueprint.route('/api/unsubscribe', methods=['POST'])
def unsubscribe():
    data = request.json
    if not data:
        log.warning("No data provided in the unsubscribe request.")
        return jsonify({"error": "No data provided."}), 400
    
    try:
        email = data.get('email')
        user = user_dao.find_by_email(email)
        
        if not user:
            log.warning(f"No user found with email: {email}")
            return jsonify({"error": "User not found"}), 404

        # Assuming you want to delete the user from the database
        user_dao.delete(user.get_id())
        log.info(f"User {user.get_id()} unsubscribed successfully")

        return jsonify({"message": "You have successfully unsubscribed."}), 200
    
    except Exception as e:
        log.error(f"Error during unsubscribe: {str(e)}")
        return jsonify({"error": "An error occurred during unsubscribe"}), 500
