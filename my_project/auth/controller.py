from .dao import *

from flask import jsonify, request

class DeveloperController:
    @staticmethod
    def get_all_developers():
        developers = DeveloperDAO.get_all_developers()
        return jsonify(developers), 200

    @staticmethod
    def get_developer(developer_id):
        developer = DeveloperDAO.get_developer_by_id(developer_id)
        if developer:
            return jsonify(developer), 200
        return jsonify({'message': 'Developer not found'}), 404

    @staticmethod
    def add_developer(data):
        if not data or not all(key in data for key in ('name', 'website', 'contact_email')):
            return jsonify({'message': 'Invalid data'}), 400
        DeveloperDAO.add_developer(data['name'], data['website'], data['contact_email'])
        return jsonify({'message': 'Developer added successfully!'}), 201

    @staticmethod
    def update_developer(developer_id, data):
        if not data or not all(key in data for key in ('name', 'website', 'contact_email')):
            return jsonify({'message': 'Invalid data'}), 400
        DeveloperDAO.update_developer(developer_id, data['name'], data['website'], data['contact_email'])
        return jsonify({'message': 'Developer updated successfully!'}), 200

    @staticmethod
    def delete_developer(developer_id):
        try:
            DeveloperDAO.delete_developer(developer_id)
            return jsonify({'message': 'Developer deleted successfully!'}), 200
        except Exception as e:
            return jsonify({'message': f'Error deleting developer: {e}'}), 500


class AppCategoryController:
    @staticmethod
    def get_all_categories():
        categories = AppCategoryDAO.get_all_categories()
        return jsonify(categories), 200

    @staticmethod
    def get_category(category_id):
        category = AppCategoryDAO.get_category_by_id(category_id)
        if category:
            return jsonify(category), 200
        return jsonify({'message': 'Category not found'}), 404

    @staticmethod
    def add_category(data):
        if not data or not all(key in data for key in ('name',)):
            return jsonify({'message': 'Invalid data'}), 400
        success = AppCategoryDAO.add_category(data['name'])
        if success:
            return jsonify({'message': 'Category added successfully!'}), 201
        return jsonify({'message': 'Failed to add category'}), 500

    @staticmethod
    def update_category(category_id, data):
        if not data or not all(key in data for key in ('name',)):
            return jsonify({'message': 'Invalid data'}), 400
        success = AppCategoryDAO.update_category(category_id, data['name'])
        if success:
            return jsonify({'message': 'Category updated successfully!'}), 200
        return jsonify({'message': 'Category not found or failed to update'}), 404

    @staticmethod
    def delete_category(category_id):
        try:
            AppCategoryDAO.delete_category(category_id)
            return jsonify({'message': 'Category deleted successfully!'}), 200
        except Exception as e:
            return jsonify({'message': f'Error deleting category: {e}'}), 500

class ApplicationController:
    @staticmethod
    def get_all_apps():
        apps = ApplicationDAO.get_all_applications()
        return jsonify(apps), 200

    @staticmethod
    def get_app(app_id):
        app = ApplicationDAO.get_application_by_id(app_id)
        if app:
            return jsonify(app), 200
        return jsonify({'message': 'App not found'}), 404

    @staticmethod
    def add_app(data):
        if not data or not all(key in data for key in ('name', 'category_id', 'release_date', 'developer_id', 'current_version')):
            return jsonify({'message': 'Invalid data'}), 400
        success = ApplicationDAO.add_application(data['name'], data['category_id'], data['release_date'], data['developer_id'], data['current_version'])
        if success:
            return jsonify({'message': 'App added successfully!'}), 201
        return jsonify({'message': 'Failed to add app'}), 500

    @staticmethod
    def update_app(app_id, data):
        if not data or not all(key in data for key in ('name', 'category_id', 'release_date', 'developer_id', 'current_version')):
            return jsonify({'message': 'Invalid data'}), 400
        success = ApplicationDAO.update_application(app_id, data['name'], data['category_id'], data['release_date'], data['developer_id'], data['current_version'])
        if success:
            return jsonify({'message': 'App updated successfully!'}), 200
        return jsonify({'message': 'App not found or failed to update'}), 404

    @staticmethod
    def delete_app(app_id):
        try:
            ApplicationDAO.delete_application(app_id)
            return jsonify({'message': 'App deleted successfully!'}), 200
        except Exception as e:
            return jsonify({'message': f'Error deleting app: {e}'}), 500


class UserController:
    def get_all_users():
        users = UserDAO.get_all_users()
        return jsonify(users), 200
        
    def get_user(user_id):
        user = UserDAO.get_user_by_id(user_id)
        if user:
            return jsonify(user), 200
        return jsonify({'message': 'User not found'}), 404
        
    def add_user(data):
        if not data or not all(key in data for key in ('username', 'email', 'password', 'signup_date')):
            return jsonify({'message': 'Invalid data'}), 400
        success = UserDAO.add_user(data['username'], data['email'], data['password'], data['signup_date'])
        if success:
            return jsonify({'message': 'User added successfully!'}), 201
        return jsonify({'message': 'Failed to add user'}), 500
    
        
    def update_user(user_id, data):
        if not data or not all(key in data for key in ('username', 'email', 'password', 'signup_date')):
            return jsonify({'message': 'Invalid data'}), 400
        success = UserDAO.update_user(user_id, data['username'], data['email'], data['password'], data['signup_date'])
        if success:
            return jsonify({'message': 'User updated successfully!'}), 200
        return jsonify({'message': 'User not found or failed to update'}), 404
        
    def delete_user(user_id):
        try:
            UserDAO.delete_user(user_id)
            return jsonify({'message': 'User deleted successfully!'}), 200
        except Exception as e:
            return jsonify({'message': f'Error deleting user: {e}'}), 500
        
