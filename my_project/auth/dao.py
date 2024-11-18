from .models import *

from flask import current_app

class DeveloperDAO:
    @staticmethod
    def get_all_developers():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM Developers")
            developers = [Developer(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching developers: {e}")
            developers = []
        finally:
            cursor.close()
        return developers
    
    @staticmethod
    def get_developer_by_id(developer_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM Developers WHERE developer_id = %s", (developer_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching developer by id: {e}")
            row = None
        finally:
            cursor.close()
        if row:
            return Developer(*row).to_dict()
        return None

    @staticmethod
    def add_developer(name, website, contact_email):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO Developers (name, website, contact_email) VALUES (%s, %s, %s)",
                (name, website, contact_email)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding developer: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def update_developer(developer_id, name, website, contact_email):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "UPDATE Developers SET name = %s, website = %s, contact_email = %s WHERE developer_id = %s",
                (name, website, contact_email, developer_id)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating developer: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def delete_developer(developer_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM Developers WHERE developer_id = %s", (developer_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting developer: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

class AppCategoryDAO:
    @staticmethod
    def get_all_categories():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM AppCategories")
            categories = [AppCategory(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching categories: {e}")
            categories = []
        finally:
            cursor.close()
        return categories
    
    @staticmethod
    def get_category_by_id(category_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM AppCategories WHERE category_id = %s", (category_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching category by id: {e}")
            row = None
        finally:
            cursor.close()
        if row:
            return AppCategory(*row).to_dict()
        return None
    
    @staticmethod
    def add_category(name):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("INSERT INTO AppCategories (name) VALUES (%s)", (name,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding category: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def update_category(category_id, name):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("UPDATE AppCategories SET name = %s WHERE category_id = %s", (name, category_id))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating category: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def delete_category(category_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM AppCategories WHERE category_id = %s", (category_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting category: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

class ApplicationDAO:
    @staticmethod
    def get_all_applications():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM Applications")
            applications = [Application(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching applications: {e}")
            applications = []
        finally:
            cursor.close()
        return applications
    
    @staticmethod
    def get_application_by_id(app_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM Applications WHERE app_id = %s", (app_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching application by id: {e}")
            row = None
        finally:
            cursor.close()
        if row:
            return Application(*row).to_dict()
        return None

    @staticmethod
    def add_application(name, category_id, release_date, developer_id, current_version):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO Applications (name, category_id, release_date, developer_id, current_version) VALUES (%s, %s, %s, %s, %s)",
                (name, category_id, release_date, developer_id, current_version)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding application: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def update_application(app_id, name, category_id, release_date, developer_id, current_version):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "UPDATE Applications SET name = %s, category_id = %s, release_date = %s, developer_id = %s, current_version = %s WHERE app_id = %s",
                (name, category_id, release_date, developer_id, current_version, app_id)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating application: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def delete_application(app_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM Applications WHERE app_id = %s", (app_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting application: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

class UserDAO:
    @staticmethod
    def get_all_users():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM Users")
            users = [User(*row).to_dict() for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching users: {e}")
            users = []
        finally:
            cursor.close()
        return users
    
    @staticmethod
    def get_user_by_id(user_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE user_id = %s", (user_id,))
            row = cursor.fetchone()
        except Exception as e:
            print(f"Error fetching user by id: {e}")
            row = None
        finally:
            cursor.close()
        if row:
            return User(*row).to_dict()
        return None

    @staticmethod
    def add_user(username, email, password, signup_date):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO Users (username, email, password, signup_date) VALUES (%s, %s, %s, %s)",
                (username, email, password, signup_date)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding user: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def update_user(user_id, username, email, password, signup_date):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "UPDATE Users SET username = %s, email = %s, password = %s, signup_date = %s WHERE user_id = %s",
                (username, email, password, signup_date, user_id)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating user: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def delete_user(user_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM Users WHERE user_id = %s", (user_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting user: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

