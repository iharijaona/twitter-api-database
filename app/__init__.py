from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    # Load config
    from config import Config
    app.config.from_object(Config)
    

    # Init databse
    from .ext.dbalchemy import db
    db.init_app(app)
    migrate = Migrate(app, db)

    # Add API
    from .apis.tweets import api as tweets
    api = Api()
    api.init_app(app)
    api.add_namespace(tweets)
    
    return app
