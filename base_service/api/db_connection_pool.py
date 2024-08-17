import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def initiate_connection_pool(app: Flask):
    db_path = os.path.join(app.instance_path, 'local_database.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SQLALCHEMY_POOL_SIZE'] = 5
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 10
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 280
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 10



def create_database(app: Flask):
    with app.app_context():
        db.create_all()  # Tworzy tabele w bazie danych na podstawie modeli
        if os.path.exists('scheme.sql'):
            with open('scheme.sql', 'r') as f:
                sql_commands = f.read()
            db.session.execute(sql_commands)
            db.session.commit()