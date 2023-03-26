from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
import os
from dotenv import load_dotenv

load_dotenv()


r = redis.Redis(
	host=os.environ.get('REDIS_HOST'),
  	port=os.environ.get('REDIS_PORT'),
  	password=os.environ.get('REDIS_PASSWORD')
)

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True

    db.init_app(app)


    from .api_endpoints import api_endpoints
    # from .flask_web_worker import pusher_endpoints
    #from .views import views
    # app.register_blueprint(flask_web_worker, url_prefix = '/')
    app.register_blueprint(api_endpoints, url_prefix = '/')
    #app.register_blueprint(views, url_prefix = "/")
    
    # from .models import User

    # @app.before_first_request
    # def create_tables():
    #     db.create_all()
    #     print("Created Database!")
    

    
    return app
