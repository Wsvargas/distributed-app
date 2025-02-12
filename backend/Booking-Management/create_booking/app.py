from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
from config import Config
from models import db_postgres
from services import create_booking_service 

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

@app.route('/booking', methods=['POST'])
def create_booking():
    """
    Create a new booking
    ---
    tags:
      - Bookings
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - user_id
            - flight_id
            - booking_date
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
      201:
        description: Booking created successfully
      400:
        description: Missing required fields
      500:
        description: Internal Server Error
    """
    data = request.get_json()
    response, status_code = create_booking_service(data)  # Llamamos a la función en `services.py`
    return jsonify(response), status_code

if __name__ == '__main__':
    with app.app_context():
        db_postgres.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5021, debug=True)
