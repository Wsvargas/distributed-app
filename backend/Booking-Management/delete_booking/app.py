from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger
from config import Config
from models import db_postgres
from services import delete_booking_service  

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

@app.route('/booking/<int:id>', methods=['DELETE'])
def delete_booking(id):
    """
    Delete a booking by ID
    ---
    tags:
      - Bookings
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Booking ID to delete
    responses:
      200:
        description: Booking deleted successfully
      404:
        description: Booking not found
      500:
        description: Internal Server Error
    """
    response, status_code = delete_booking_service(id)
    return jsonify(response), status_code

if __name__ == '__main__':
    with app.app_context():
        db_postgres.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5024, debug=True)
