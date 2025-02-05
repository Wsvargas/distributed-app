from flask import Flask, jsonify
from config import Config
from models import db_postgres, Flight

app = Flask(__name__)
app.config.from_object(Config)
db_postgres.init_app(app)

@app.route('/flights/<int:id>', methods=['GET'])
def get_flight(id):
    flight = Flight.query.get(id)
    if not flight:
        return jsonify({"message": "Flight not found"}), 404

    return jsonify({
        "id": flight.id,
        "origin": flight.origin,
        "destination": flight.destination,
        "departure_time": flight.departure_time,
        "arrival_time": flight.arrival_time,
        "price": str(flight.price),
        "status": flight.status,
        "available_seats": flight.available_seats
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5033, debug=True)
