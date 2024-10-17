from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Target(db.Model):
    __tablename__ = 'targets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ip_address = db.Column(db.String(45), unique=True, nullable=False)
    port = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ip_address": self.ip_address,
            "port": self.port,
            "description": self.description,
        }
