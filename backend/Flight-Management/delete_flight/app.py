from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger
from config import Config
from models import db_postgres
from services import delete_flight_service 

app = Flask(__name__)
app.config.from_object(Config)
db_postgres.init_app(app)
CORS(app)
swagger = Swagger(app)

@app.route('/health', methods=['GET'])
def health():
    """
    Health Check
    ---
    responses:
      200:
        description: API is running
    """
    return jsonify(status="ok"), 200

@app.route('/flights/<int:id>', methods=['DELETE'])
def delete_flight(id):
    """
    Delete a flight by ID
    ---
    tags:
      - Flights
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Flight ID to delete
    responses:
      200:
        description: Flight deleted successfully
      404:
        description: Flight not found
      500:
        description: Internal Server Error
    """
    response, status_code = delete_flight_service(id)
    return jsonify(response), status_code

if __name__ == '__main__':
    with app.app_context():
        db_postgres.create_all()

    app.run(host='0.0.0.0', port=5035, debug=True)
