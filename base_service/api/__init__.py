import os

from flask import Flask
from flasgger import Swagger
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    api = Api(app)
    swagger = Swagger(
        app,
        template={
            "info": {
                "title": "Remote Scanner Base Service",
                "description": "Base Service monitors status of other services and provides them information about the others.",
                "version": "0.0.1",
            }
        },
    )

    from . import alive

    api.add_resource(alive.Alive, "/alive")

    from . import service_registration

    api.add_resource(service_registration.ServiceRegistrationPost, "/service")
    api.add_resource(service_registration.ServiceRegistration, "/service/<int:id>")

    from .db_connection_pool import initiate_connection_pool, create_database, db
    initiate_connection_pool(app)
    db.init_app(app)
    create_database(app)

    return app
