class Developer:
    def __init__(self, developer_id, name, website, contact_email):
        self.developer_id = developer_id
        self.name = name
        self.website = website
        self.contact_email = contact_email

    def to_dict(self):
        return {
            'developer_id': self.developer_id,
            'name': self.name,
            'website': self.website,
            'contact_email': self.contact_email
        }

class AppCategory:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name
    
    def to_dict(self):
        return {
            'category_id': self.category_id,
            'name': self.name
        }
    
class Application:
    def __init__(self, app_id, name, category_id, release_date, developer_id, current_version):
        self.app_id = app_id
        self.name = name
        self.category_id = category_id
        self.release_date = release_date
        self.developer_id = developer_id
        self.current_version = current_version

    def to_dict(self):
        return {
            'app_id': self.app_id,
            'name': self.name,
            'category_id': self.category_id,
            'release_date': self.release_date,
            'developer_id': self.developer_id,
            'current_version': self.current_version
        }
    
class User:
    def __init__(self, user_id, username, email, password, signup_date):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.signup_date = signup_date

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'signup_date': self.signup_date
        }
    
class Review:
    def __init__(self, review_id, app_id, user_id, review_text, review_date):
        self.review_id = review_id
        self.app_id = app_id
        self.user_id = user_id
        self.review_text = review_text
        self.review_date = review_date

    def to_dict(self):
        return {
            'review_id': self.review_id,
            'app_id': self.app_id,
            'user_id': self.user_id,
            'review_text': self.review_text,
            'review_date': self.review_date
        }
    
class Rating:
    def __init__(self, rating_id, app_id, user_id, rating_value, rating_date):
        self.rating_id = rating_id
        self.app_id = app_id
        self.user_id = user_id
        self.rating_value = rating_value
        self.rating_date = rating_date

    def to_dict(self):
        return {
            'rating_id': self.rating_id,
            'app_id': self.app_id,
            'user_id': self.user_id,
            'rating_value': self.rating_value,
            'rating_date': self.rating_date
        }
    
class Device:
    def __init__(self, device_id, user_id, device_model, os_version):
        self.device_id = device_id
        self.user_id = user_id
        self.device_model = device_model
        self.os_version = os_version

    def to_dict(self):
        return {
            'device_id': self.device_id,
            'user_id': self.user_id,
            'device_model': self.device_model,
            'os_version': self.os_version
        }

class Install:
    def __init__(self, install_id, app_id, user_id, install_date, device_id):
        self.install_id = install_id
        self.app_id = app_id
        self.user_id = user_id
        self.install_date = install_date
        self.device_id = device_id

    def to_dict(self):
        return {
            'install_id': self.install_id,
            'app_id': self.app_id,
            'user_id': self.user_id,
            'install_date': self.install_date,
            'device_id': self.device_id
        }

class AppUpdate:
    def __init__(self, update_id, app_id, update_version, update_date):
        self.update_id = update_id
        self.app_id = app_id
        self.update_version = update_version
        self.update_date = update_date

    def to_dict(self):
        return {
            'update_id': self.update_id,
            'app_id': self.app_id,
            'update_version': self.update_version,
            'update_date': self.update_date
        }

class PurchaseHistory:
    def __init__(self, purchase_id, user_id, app_id, purchase_date, purchase_amount):
        self.purchase_id = purchase_id
        self.user_id = user_id
        self.app_id = app_id
        self.purchase_date = purchase_date
        self.purchase_amount = purchase_amount

    def to_dict(self):
        return {
            'purchase_id': self.purchase_id,
            'user_id': self.user_id,
            'app_id': self.app_id,
            'purchase_date': self.purchase_date,
            'purchase_amount': self.purchase_amount
        }
