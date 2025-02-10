from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from models import db_postgres, Flight

app = Flask(__name__)
app.config.from_object(Config)
db_postgres.init_app(app)
CORS(app)

@app.route('/flights', methods=['GET'])
def get_flights():
    flights = Flight.query.all()
    return jsonify([
        {
            "id": f.id,
            "origin": f.origin,
            "destination": f.destination,
            "departure_time": f.departure_time,
            "arrival_time": f.arrival_time,
            "price": str(f.price),
            "status": f.status,
            "available_seats": f.available_seats
        } for f in flights
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5032, debug=True)
