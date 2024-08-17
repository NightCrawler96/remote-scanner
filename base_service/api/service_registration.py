from dataclasses import dataclass
from flask import jsonify, request
from flask_restful import Resource
from .db_models import *

@dataclass
class ServiceRegistrationDto:
    id: int
    service_name: str
    host_name: str
    port: int
    alive_path: str
    health_check_path: str

class ServiceRegistration(Resource):
    def post(self, id):
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
        new_service: ServiceRegistrationDto = ServiceRegistrationDto(**(request.get_json()))
        service = Service()
        service.service_name = new_service.service_name
        service.host_name = new_service.host_name
        service.port = new_service.port
        service.alive_path = new_service.alive_path
        service.health_check_path = new_service.health_check_path
        with db.session as sess:
            sess.add(service)
            sess.commit()

        return jsonify(service), 201
    
    # def delete(self, id):
    #     """
    #     This is enpoint used to remove service.
    #     ---
    #     tags:
    #         - Service
    #     parameters:
    #         -   in: "path"
    #             name: "id"
    #             type: "integer"
    #             required: true
    #     responses:
    #         204:
    #             description: Service was deleted successfully.
    #     """
    #     with get_connection() as conn:
    #         conn.execute(
    #             'DELETE FROM service_registration WHERE id = ?',
    #             id
    #         )
    #         conn.commit()
    #         close_db()

    #     return None, 204
