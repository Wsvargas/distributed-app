from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
from config import Config
from models import db_postgres
from services import update_flight_service 

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

@app.route('/flights/<int:id>', methods=['PUT'])
def update_flight(id):
    """
    Update a flight by ID
    ---
    tags:
      - Flights
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Flight ID to update
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            origin:
              type: string
              example: "New York"
            destination:
              type: string
              example: "Los Angeles"
            departure_time:
              type: string
              format: date-time
              example: "2025-02-11T12:30:00"
            arrival_time:
              type: string
              format: date-time
              example: "2025-02-11T15:30:00"
            price:
              type: number
              format: float
              example: 299.99
            status:
              type: string
              example: "active"
            available_seats:
              type: integer
              example: 100
    responses:
      200:
        description: Flight updated successfully
      404:
        description: Flight not found
      500:
        description: Internal Server Error
    """
    data = request.get_json()
    response, status_code = update_flight_service(id, data)
    return jsonify(response), status_code

if __name__ == '__main__':
    with app.app_context():
        db_postgres.create_all()

    app.run(host='0.0.0.0', port=5034, debug=True)
