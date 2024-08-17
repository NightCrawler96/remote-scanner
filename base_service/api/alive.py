import flask
from flask_restful import Resource


class Alive(Resource):
    def get(self):
        """
        This is enpoint used to monitor service's status
        ---
        tags:
            - Status
        decscription: Returns 'ALIVE' status when running.
        responses:
            200:
                description: Service is alive.
                schema:
                    type: string
                examples:
                    "ALIVE"
        """
        response = flask.make_response("ALIVE")
        response.headers["content-type"] = "plain/text"
        return response