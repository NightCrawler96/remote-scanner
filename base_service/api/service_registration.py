from dataclasses import dataclass
import datetime
from sqlalchemy.exc import NoResultFound
from flask import request
from flask_restful import Resource
from .db_connection_pool import db


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(16), unique=True, nullable=False)
    host_name = db.Column(db.String(16), nullable=False)
    port = db.Column(db.String(16), nullable=False)
    alive_path = db.Column(db.String(16), nullable=False)
    health_check_path = db.Column(db.String(16), nullable=False)
    status = db.Column(db.String(16), nullable=False, default="ALIVE")
    last_check = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now(datetime.UTC))

    __table_args__ = (
        db.UniqueConstraint("host_name", "port", name="unique_host_port"),
    )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "service_name": self.service_name,
            "host_name": self.host_name,
            "port": self.port,
            "alive_path": self.alive_path,
            "health_check_path": self.health_check_path,
            "status": self.status,
            "last_check": self.last_check.isoformat()
        }


@dataclass
class ServiceRegistrationDto:
    id: int
    service_name: str
    host_name: str
    port: int
    alive_path: str
    health_check_path: str


class ServiceRegistrationPost(Resource):
    def post(self):
        """
        This is enpoint used to register new services.
        ---
        tags:
            - Service
        description: Adds new service.
        definitions:
            ServiceRegistrationDto:
                type: "object"
                properties:
                    id:
                        type: "integer"
                    service_name:
                        type: "string"
                        example: "New Service"
                    host_name:
                        type: "string"
                        example: "newservice"
                    port:
                        type: "integer"
                        example: 5000
                    alive_path:
                        type: "string"
                        example: "/alive"
                    health_check_path:
                        type: "string"
                        example: "/healthcheck"
        parameters:
            -   in: "body"
                name: "service"
                description: "New service definition"
                required: true
                schema:
                    $ref: "#/definitions/ServiceRegistrationDto"
        responses:
            201:
                description: Service was registeed successfully.
                schema:
                    $ref: '#/definitions/ServiceRegistrationDto'
        """
        new_service: ServiceRegistrationDto = ServiceRegistrationDto(
            **(request.get_json())
        )
        service = Service(
            service_name=new_service.service_name,
            host_name=new_service.host_name,
            port=new_service.port,
            alive_path=new_service.alive_path,
            health_check_path=new_service.health_check_path,
        )

        db.session.add(service)
        db.session.commit()

        return service.to_dict(), 201


class ServiceRegistration(Resource):

    def delete(self, id):
        """
        This is enpoint used to remove service.
        ---
        tags:
            - Service
        parameters:
            -   in: "path"
                name: "id"
                type: "integer"
                required: true
        responses:
            204:
                description: Service was deleted successfully.
        """

        Service.query.filter_by(id=id).delete()
        db.session.commit()

        return None, 204

    def put(self, id):
        """
        This is enpoint used to modify service.
        ---
        tags:
            - Service
        parameters:
            -   in: "path"
                name: "id"
                type: "integer"
                required: true
        responses:
            200:
                description: Service was deleted updated.
        """
        try:
            service = Service.query.filter_by(id=id).one()
            return service.to_dict(), 200
        except NoResultFound as e:
            return {"details": "Service with this id doesn't exist."}, 400
