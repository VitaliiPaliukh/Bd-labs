
from flask import Blueprint, jsonify, request
from auth.dao.user_dao import UserDAO

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user', methods=['POST'])
def create_user():
    """
    Create a new user
    ---
    tags:
      - Users
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        description: User object
        schema:
          type: object
          required:
            - username
            - email
          properties:
            username:
              type: string
              example: vitalik
            email:
              type: string
              example: vitalii@example.com
            password:
              type: string
              example: mySecret123
    responses:
      201:
        description: User created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            username:
              type: string
              example: vitalik
            email:
              type: string
              example: vitalii@example.com
      400:
        description: Invalid input
    """
    data = request.get_json()
    user_dto = UserDAO.create_user(data['username'], data['email'], data['password'])
    return jsonify(user_dto.to_dict()), 201

@user_bp.route('/users', methods=['GET'])
def get_users():
    """
        Get all users
        ---
        responses:
          200:
            description: A list of users
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  name:
                    type: string
        """
    users = UserDAO.get_all_users()
    return jsonify([user.to_dict() for user in users]), 200

