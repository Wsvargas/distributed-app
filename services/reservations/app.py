from flask import Flask, request, jsonify
from models import db, Reservation
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    new_reservation = Reservation(
        flight_number=data['flight_number'],
        customer_name=data['customer_name'],
        seats_reserved=data['seats_reserved']
    )
    db.session.add(new_reservation)
    db.session.commit()
    return jsonify({"message": "Reservation created successfully"}), 201

@app.route('/reservations', methods=['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    result = [
        {
            "id": res.id,
            "flight_number": res.flight_number,
            "customer_name": res.customer_name,
            "seats_reserved": res.seats_reserved,
            "status": res.status
        }
        for res in reservations
    ]
    return jsonify(result), 200

@app.route('/reservations/<int:id>', methods=['PUT'])
def update_reservation(id):
    data = request.get_json()
    reservation = Reservation.query.get_or_404(id)
    reservation.status = data.get('status', reservation.status)
    db.session.commit()
    return jsonify({"message": "Reservation updated successfully"}), 200

@app.route('/reservations/<int:id>', methods=['DELETE'])
def delete_reservation(id):
    reservation = Reservation.query.get_or_404(id)
    db.session.delete(reservation)
    db.session.commit()
    return jsonify({"message": "Reservation deleted successfully"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
