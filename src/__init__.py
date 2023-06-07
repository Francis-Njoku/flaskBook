from flask import Flask
import os
from src.auth import auth
from src.bookmarks import bookmarks

def create_app(test_confg=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_confg is None:

        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
        )
    else:
        app.config.from_mapping(test_confg) 

    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)    

    
    @app.route("/", methods=["GET"])
    def index():
        return "Hello world"

    @app.route("/hello", methods=["GET"])
    def hello():
        return {"Message": "Hello World"} 

        
              
    return app          
