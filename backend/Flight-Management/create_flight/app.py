from flask import Flask, request, jsonify
from config import Config
from models import db_postgres, Flight
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db_postgres.init_app(app)

@app.route('/flights', methods=['POST'])
def create_flight():
    data = request.get_json()

    try:
        new_flight = Flight(
            origin=data["origin"],
            destination=data["destination"],
            departure_time=datetime.strptime(data["departure_time"], '%Y-%m-%dT%H:%M:%S'),
            arrival_time=datetime.strptime(data["arrival_time"], '%Y-%m-%dT%H:%M:%S'),
            price=data["price"],
            total_seats=data["total_seats"],
            available_seats=data["total_seats"]
        )

        db_postgres.session.add(new_flight)
        db_postgres.session.commit()
        return jsonify({'message': 'Flight created successfully'}), 201

    except Exception as e:
        db_postgres.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db_postgres.create_all()
    
    app.run(host='0.0.0.0', port=5031, debug=True)
