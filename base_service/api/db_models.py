from .db_connection_pool import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(16), unique=True, nullable=False)
    host_name = db.Column(db.String(16), nullable=False)
    port = db.Column(db.String(16), nullable=False)
    alive_path = db.Column(db.String(16), nullable=False)
    health_check_path = db.Column(db.String(16), nullable=False)
    status = db.relationship('ServiceStatus', backref='service', lazy=True)

    __table_args__ = (db.UniqueConstraint('host_name', 'port', name='unique_host_port'),)

class ServiceStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)