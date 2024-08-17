import os

from flask import Flask
from flasgger import Swagger
from flask_restful import Api

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'api.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    api = Api(app)
    swagger = Swagger(app, template={
            "info":{
                "title": "Remote Scanner Base Service",
                "description": "Base Service monitors status of other services and provides them information about the others.",
                "version": "0.0.1"
            }
    })

    
    from . import alive
    api.add_resource(alive.Alive, "/alive")
    
    from . import db
    db.init_app(app)

    

    return app
