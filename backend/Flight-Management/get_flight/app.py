from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger
from config import Config
from models import db_postgres
from services import get_flight_service  

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

@app.route('/flights/<int:id>', methods=['GET'])
def get_flight(id):
    """
    Get a flight by ID
    ---
    tags:
      - Flights
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Flight ID to retrieve
    responses:
      200:
        description: Flight retrieved successfully
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
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
      404:
        description: Flight not found
      500:
        description: Internal Server Error
    """
    response, status_code = get_flight_service(id)
    return jsonify(response), status_code

if __name__ == '__main__':
    with app.app_context():
        db_postgres.create_all()

    app.run(host='0.0.0.0', port=5033, debug=True)
