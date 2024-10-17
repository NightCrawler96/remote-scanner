from flask import Flask
from flasgger import Swagger
from config import Config
from models import db
from .routes import vulns_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(vulns_bp)

    swagger = Swagger(app)
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
