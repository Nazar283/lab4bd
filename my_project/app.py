import os
from flask import Flask, current_app
from flask_mysqldb import MySQL
from auth.route import api_bp

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0322753890nazar'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'googleplaystoredb'

app.config['MYSQL_SSL_DISABLED'] = True

app.mysql = mysql

with app.app_context():
    try:
        connection = mysql.connection
        cursor = connection.cursor()
        cursor.execute("SELECT 1")  # Тестовий запит
        cursor.close()
        print("Successfully connected to the database.")
    except Exception as e:
        print(f"Error connecting to the database: {e}")

app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
