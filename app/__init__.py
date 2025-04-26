from flask import Flask
from .config import AppConfigrations
from .extensions import db , login_manager , bcrypt
from routes import auth , estates , admin




def create_app():
    app = Flask(__name__ , static_folder='/static' , template_folder = "/template")
    app.config.from_object(AppConfigrations)

    app.register_blueprint(auth)
    app.register_blueprint(estates)
    app.register_blueprint(admin)
    
    login_manager.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)

    with app.app_context() as cnx:
        db.create_all()

    return app




