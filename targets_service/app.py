from flask import Flask
from flasgger import Swagger
from config import Config
from models import db
from routes import targets_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(targets_bp)

    swagger = Swagger(app)
    return app

# Expose the app for WSGI (Gunicorn)
app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
