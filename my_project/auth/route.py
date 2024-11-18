from flask import Blueprint, request
from .controller import *

api_bp = Blueprint('api', __name__)

@api_bp.route('/developers', methods=['GET'])
def get_all_developers():
    return DeveloperController.get_all_developers()

@api_bp.route('/developers/<int:developer_id>', methods=['GET'])
def get_developer(developer_id):
    return DeveloperController.get_developer(developer_id)

@api_bp.route('/developers', methods=['POST'])
def add_developer():
    data = request.get_json()
    print(data)
    return DeveloperController.add_developer(data)

@api_bp.route('/developers/<int:developer_id>', methods=['PUT'])
def update_developer(developer_id):
    data = request.get_json()
    return DeveloperController.update_developer(developer_id, data)

@api_bp.route('/developers/<int:developer_id>', methods=['DELETE'])
def delete_developer(developer_id):

    return DeveloperController.delete_developer(developer_id)

@api_bp.route('/app-categories', methods=['GET'])
def get_all_categories():
    return AppCategoryController.get_all_categories()

@api_bp.route('/app-categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    return AppCategoryController.get_category(category_id)

@api_bp.route('/app-categories', methods=['POST'])
def add_category():
    data = request.get_json()
    return AppCategoryController.add_category(data)

@api_bp.route('/app-categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.get_json()
    return AppCategoryController.update_category(category_id, data)

@api_bp.route('/app-categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    return AppCategoryController.delete_category(category_id)

@api_bp.route('/applications', methods=['GET'])
def get_all_applications():
    return ApplicationController.get_all_apps()

@api_bp.route('/applications/<int:app_id>', methods=['GET'])
def get_application(app_id):
    return ApplicationController.get_app(app_id)

@api_bp.route('/applications', methods=['POST'])
def add_application():
    data = request.get_json()
    return ApplicationController.add_app(data)

@api_bp.route('/applications/<int:app_id>', methods=['PUT'])
def update_application(app_id):
    data = request.get_json()
    return ApplicationController.update_app(app_id, data)

@api_bp.route('/applications/<int:app_id>', methods=['DELETE'])
def delete_application(app_id):
    return ApplicationController.delete_app(app_id)

@api_bp.route('/users', methods=['GET'])
def get_all_users():
    return UserController.get_all_users()

@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return UserController.get_user(user_id)

@api_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    return UserController.add_user(data)

@api_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return UserController.update_user(user_id, data)

@api_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UserController.delete_user(user_id)