from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
from config import Config
from models import db_postgres
from services import update_booking_service

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

@app.route('/booking/<int:id>', methods=['PUT'])
def update_booking(id):
    """
    Update a booking
    ---
    tags:
      - Bookings
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Booking ID to update
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            user_id:
              type: integer
              example: 123
            flight_id:
              type: integer
              example: 456
            booking_date:
              type: string
              format: date-time
              example: "2025-02-11T12:30:00"
            status:
              type: string
              example: "confirmed"
    responses:
      200:
        description: Booking updated successfully
      400:
        description: Bad request (missing fields)
      404:
        description: Booking not found
      500:
        description: Internal Server Error
    """
    data = request.get_json()
    response, status_code = update_booking_service(id, data)
    return jsonify(response), status_code

if __name__ == '__main__':
    with app.app_context():
        db_postgres.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5023, debug=True)
