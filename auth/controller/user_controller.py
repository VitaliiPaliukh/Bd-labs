# У файлі auth/controller/user_controller.py

from flask import Blueprint, jsonify, request
from auth.dao.user_dao import UserDAO

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_dto = UserDAO.create_user(data['username'], data['email'], data['password'])
    return jsonify(user_dto.to_dict()), 201

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = UserDAO.get_all_users()  # This now returns a list of UserDTO instances
    return jsonify([user.to_dict() for user in users]), 200  # Convert to dictionary for JSON

