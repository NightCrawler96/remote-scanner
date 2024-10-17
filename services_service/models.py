from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    target_id = db.Column(db.Integer, nullable=False)  # Refers to target ID from `targets_service`
    name = db.Column(db.String(100), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='running')
    description = db.Column(db.String(255))

    def to_dict(self):
        return {
            "id": self.id,
            "target_id": self.target_id,
            "name": self.name,
            "port": self.port,
            "status": self.status,
            "description": self.description,
        }
