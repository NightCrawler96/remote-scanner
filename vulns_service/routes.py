import logging
from flask import Blueprint, request, jsonify
from models import db, Vulnerability


vulns_bp = Blueprint('vulnerabilities', __name__)

@vulns_bp.route('/vulnerabilities', methods=['POST'])
def create_vulnerability():
    """Create a new vulnerability
    ---
    tags:
      - Vulnerabilities
    parameters:
      - name: service_id
        in: formData
        type: integer
        required: true
      - name: name
        in: formData
        type: string
        required: true
      - name: severity
        in: formData
        type: string
        required: true
      - name: description
        in: formData
        type: string
        required: false
      - name: status
        in: formData
        type: string
        required: false
    responses:
      201:
        description: Vulnerability created successfully
      400:
        description: Bad request
    """
    data = request.json
    try:
        new_vuln = Vulnerability(
            service_id=data['service_id'],
            name=data['name'],
            severity=data['severity'],
            description=data.get('description'),
            status=data.get('status', 'open')
        )
        db.session.add(new_vuln)
        db.session.commit()
        return jsonify(new_vuln.to_dict()), 201
    except Exception as e:
        logging.error("Error creating vulnerability: %s", e, exc_info=True)
        return jsonify({'error': 'An internal error has occurred!'}), 400

@vulns_bp.route('/vulnerabilities', methods=['GET'])
def get_vulnerabilities():
    """Get a list of all vulnerabilities
    ---
    tags:
      - Vulnerabilities
    responses:
      200:
        description: List of vulnerabilities
    """
    vulns = Vulnerability.query.all()
    return jsonify([vuln.to_dict() for vuln in vulns]), 200

@vulns_bp.route('/vulnerabilities/<int:id>', methods=['GET'])
def get_vulnerability(id):
    """Get a vulnerability by ID
    ---
    tags:
      - Vulnerabilities
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Vulnerability found
      404:
        description: Vulnerability not found
    """
    vuln = Vulnerability.query.get_or_404(id)
    return jsonify(vuln.to_dict()), 200

@vulns_bp.route('/vulnerabilities/<int:id>', methods=['PUT'])
def update_vulnerability(id):
    """Update a vulnerability by ID
    ---
    tags:
      - Vulnerabilities
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Vulnerability updated successfully
      404:
        description: Vulnerability not found
      400:
        description: Bad request
    """
    vuln = Vulnerability.query.get_or_404(id)
    data = request.json
    try:
        vuln.name = data.get('name', vuln.name)
        vuln.severity = data.get('severity', vuln.severity)
        vuln.description = data.get('description', vuln.description)
        vuln.status = data.get('status', vuln.status)
        db.session.commit()
        return jsonify(vuln.to_dict()), 200
    except Exception as e:
        logging.error("Error updating vulnerability: %s", e, exc_info=True)
        return jsonify({'error': 'An internal error has occurred!'}), 400

@vulns_bp.route('/vulnerabilities/<int:id>', methods=['DELETE'])
def delete_vulnerability(id):
    """Delete a vulnerability by ID
    ---
    tags:
      - Vulnerabilities
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Vulnerability deleted successfully
      404:
        description: Vulnerability not found
    """
    vuln = Vulnerability.query.get_or_404(id)
    db.session.delete(vuln)
    db.session.commit()
    return '', 204
