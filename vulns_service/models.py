from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vulnerability(db.Model):
    __tablename__ = 'vulnerabilities'

    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, nullable=False)  # Refers to service ID from `services_service`
    name = db.Column(db.String(100), nullable=False)
    severity = db.Column(db.String(20), nullable=False)  # E.g., 'low', 'medium', 'high', 'critical'
    description = db.Column(db.String(255))
    status = db.Column(db.String(50), nullable=False, default='open')  # E.g., 'open', 'closed'

    def to_dict(self):
        return {
            "id": self.id,
            "service_id": self.service_id,
            "name": self.name,
            "severity": self.severity,
            "description": self.description,
            "status": self.status,
        }
