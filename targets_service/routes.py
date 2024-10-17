from flask import Blueprint, request, jsonify
from models import db, Target

targets_bp = Blueprint('targets', __name__)

@targets_bp.route('/targets', methods=['POST'])
def create_target():
    """Create a new target server
    ---
    tags:
      - Targets
    parameters:
      - name: name
        in: formData
        type: string
        required: true
      - name: ip_address
        in: formData
        type: string
        required: true
      - name: port
        in: formData
        type: integer
        required: true
      - name: description
        in: formData
        type: string
    responses:
      201:
        description: Target created successfully
      400:
        description: Bad request
    """
    data = request.json
    try:
        new_target = Target(
            name=data['name'],
            ip_address=data['ip_address'],
            port=data['port'],
            description=data.get('description')
        )
        db.session.add(new_target)
        db.session.commit()
        return jsonify(new_target.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@targets_bp.route('/targets', methods=['GET'])
def get_targets():
    """Get a list of all targets
    ---
    tags:
      - Targets
    responses:
      200:
        description: List of targets
    """
    targets = Target.query.all()
    return jsonify([target.to_dict() for target in targets]), 200

@targets_bp.route('/targets/<int:id>', methods=['GET'])
def get_target(id):
    """Get a target by ID
    ---
    tags:
      - Targets
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Target found
      404:
        description: Target not found
    """
    target = Target.query.get_or_404(id)
    return jsonify(target.to_dict()), 200

@targets_bp.route('/targets/<int:id>', methods=['PUT'])
def update_target(id):
    """Update a target by ID
    ---
    tags:
      - Targets
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Target updated successfully
      404:
        description: Target not found
      400:
        description: Bad request
    """
    target = Target.query.get_or_404(id)
    data = request.json
    try:
        target.name = data.get('name', target.name)
        target.ip_address = data.get('ip_address', target.ip_address)
        target.port = data.get('port', target.port)
        target.description = data.get('description', target.description)
        db.session.commit()
        return jsonify(target.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@targets_bp.route('/targets/<int:id>', methods=['DELETE'])
def delete_target(id):
    """Delete a target by ID
    ---
    tags:
      - Targets
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Target deleted successfully
      404:
        description: Target not found
    """
    target = Target.query.get_or_404(id)
    db.session.delete(target)
    db.session.commit()
    return '', 204
