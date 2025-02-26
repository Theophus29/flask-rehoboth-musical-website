from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()  # Define MySQL globally

def create_app():
    app = Flask(__name__)

    # App configuration
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'Theophus@29'
    app.config['MYSQL_DB'] = 'rehoboth'

    # Initialize MySQL
    mysql.init_app(app)

    # Import blueprints
    from app.admin_routes import admin_bp
    from app.stud_routes import stud_bp
    from app.auth_routes import auth_bp
    from app.staff_routes import staff_bp

    # Register blueprints
    app.register_blueprint(admin_bp)
    app.register_blueprint(stud_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(staff_bp)

    return app
