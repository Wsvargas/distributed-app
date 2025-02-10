from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
from models import db_postgres, Booking
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db_postgres.init_app(app)
CORS(app)

@app.route('/booking/<int:id>', methods=['PUT'])
def update_booking(id):
    data = request.get_json()
    user_id = data.get('user_id')
    flight_id = data.get('flight_id')
    booking_date = data.get('booking_date')
    status = data.get('status')

    if not any([user_id, flight_id, booking_date, status]):
        return jsonify({'error': 'At least one field (user_id, flight_id, booking_date, status) is required for update.'}), 400

    booking = Booking.query.get(id)
    if not booking:
        return jsonify({'error': 'Booking not found.'}), 404

    try:
        if user_id:
            booking.user_id = user_id
        if flight_id:
            booking.flight_id = flight_id
        if booking_date:
            booking.booking_date = datetime.strptime(booking_date, '%Y-%m-%d').date()
        if status:
            booking.status = status 

        db_postgres.session.commit()
        return jsonify({'message': 'Booking updated successfully.'}), 200
    except Exception as e:
        db_postgres.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db_postgres.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5023, debug=True)