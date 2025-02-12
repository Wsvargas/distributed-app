from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
from config import Config
from models import db_postgres
from services import create_flight_service 

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

@app.route('/flights', methods=['POST'])
def create_flight():
    """
    Create a new flight
    ---
    tags:
      - Flights
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - origin
            - destination
            - departure_time
            - arrival_time
            - price
            - total_seats
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
            total_seats:
              type: integer
              example: 200
    responses:
      201:
        description: Flight created successfully
      400:
        description: Bad request (missing fields)
      500:
        description: Internal Server Error
    """
    data = request.get_json()
    response, status_code = create_flight_service(data)
    return jsonify(response), status_code

if __name__ == '__main__':
    with app.app_context():
        db_postgres.create_all()

    app.run(host='0.0.0.0', port=5031, debug=True)
