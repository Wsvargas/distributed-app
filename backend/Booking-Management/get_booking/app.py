from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger
from config import Config
from models import db_postgres
from services import get_all_bookings

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

@app.route('/booking', methods=['GET'])
def get_booking():
    """
    Get all bookings
    ---
    tags:
      - Bookings
    responses:
      200:
        description: Returns a list of all bookings
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
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
      500:
        description: Internal Server Error
    """
    response, status_code = get_all_bookings()
    return jsonify(response), status_code

if __name__ == '__main__':
    with app.app_context():
        db_postgres.create_all()
        print("Tables created successfully.")

    app.run(host='0.0.0.0', port=5022, debug=True)
