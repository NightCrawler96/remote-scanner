from flask import Blueprint, request, jsonify
from models import db, Service
import logging
services_bp = Blueprint('services', __name__)

@services_bp.route('/services', methods=['POST'])
def create_service():
    """Create a new service
    ---
    tags:
      - Services
    parameters:
      - name: target_id
        in: formData
        type: integer
        required: true
      - name: name
        in: formData
        type: string
        required: true
      - name: port
        in: formData
        type: integer
        required: true
      - name: status
        in: formData
        type: string
        required: false
      - name: description
        in: formData
        type: string
        required: false
    responses:
      201:
        description: Service created successfully
      400:
        description: Bad request
    """
    data = request.json
    try:
        new_service = Service(
            target_id=data['target_id'],
            name=data['name'],
            port=data['port'],
            status=data.get('status', 'running'),
            description=data.get('description')
        )
        db.session.add(new_service)
        db.session.commit()
        return jsonify(new_service.to_dict()), 201
    except Exception as e:
        logging.error("Error creating service: %s", e)
        return jsonify({'error': 'An internal error has occurred!'}), 400

@services_bp.route('/services', methods=['GET'])
def get_services():
    """Get a list of all services
    ---
    tags:
      - Services
    responses:
      200:
        description: List of services
    """
    services = Service.query.all()
    return jsonify([service.to_dict() for service in services]), 200

@services_bp.route('/services/<int:id>', methods=['GET'])
def get_service(id):
    """Get a service by ID
    ---
    tags:
      - Services
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Service found
      404:
        description: Service not found
    """
    service = Service.query.get_or_404(id)
    return jsonify(service.to_dict()), 200

@services_bp.route('/services/<int:id>', methods=['PUT'])
def update_service(id):
    """Update a service by ID
    ---
    tags:
      - Services
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Service updated successfully
      404:
        description: Service not found
      400:
        description: Bad request
    """
    service = Service.query.get_or_404(id)
    data = request.json
    try:
        service.name = data.get('name', service.name)
        service.port = data.get('port', service.port)
        service.status = data.get('status', service.status)
        service.description = data.get('description', service.description)
        db.session.commit()
        return jsonify(service.to_dict()), 200
    except Exception as e:
        logging.error("Error updating service: %s", e)
        return jsonify({'error': 'An internal error has occurred!'}), 400

@services_bp.route('/services/<int:id>', methods=['DELETE'])
def delete_service(id):
    """Delete a service by ID
    ---
    tags:
      - Services
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Service deleted successfully
      404:
        description: Service not found
    """
    service = Service.query.get_or_404(id)
    db.session.delete(service)
    db.session.commit()
    return '', 204
