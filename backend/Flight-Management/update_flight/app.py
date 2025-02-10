from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Config
from models import db_postgres, Flight

app = Flask(__name__)
app.config.from_object(Config)
db_postgres.init_app(app)
CORS(app)

@app.route('/flights/<int:id>', methods=['PUT'])
def update_flight(id):
    flight = Flight.query.get(id)
    if not flight:
        return jsonify({"message": "Flight not found"}), 404

    data = request.get_json()
    
    flight.origin = data.get("origin", flight.origin)
    flight.destination = data.get("destination", flight.destination)
    flight.departure_time = data.get("departure_time", flight.departure_time)
    flight.arrival_time = data.get("arrival_time", flight.arrival_time)
    flight.price = data.get("price", flight.price)
    flight.status = data.get("status", flight.status)
    flight.available_seats = data.get("available_seats", flight.available_seats)

    try:
        db_postgres.session.commit()
        return jsonify({"message": "Flight updated successfully"}), 200
    except Exception as e:
        db_postgres.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5034, debug=True)
