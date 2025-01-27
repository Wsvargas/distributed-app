from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# PostgreSQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db_postgres:5432/booking_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_postgres = SQLAlchemy(app)

# Bookng model with additional characteristics
class Booking(db_postgres.Model):
    id = db_postgres.Column(db_postgres.Integer, primary_key=True)
    user_id = db_postgres.Column(db_postgres.Integer, nullable=False)
    flight_id = db_postgres.Column(db_postgres.Integer, nullable=False)
    booking_date = db_postgres.Column(db_postgres.DateTime, nullable=False)
    status = db_postgres.Column(db_postgres.String(50), nullable=False)

@app.route('/booking/<int:id>', methods=['PUT'])
def update_booking(id):
    data = request.get_json()
    user_id = data.get('user_id')
    flight_id = data.get('flight_id')
    booking_date = data.get('booking_date')
    status = data.get('status')

    # Ensure at least one field is provided for update
    if not any([user_id, flight_id, booking_date, status]):
        return jsonify({'error': 'At least one field (user_id, flight_id, booking_date, status) is required for update.'}), 400

    booking = Booking.query.get(id)
    if not  booking:
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
    # Create tables within the application context (if necessary)
    with app.app_context():
        db_postgres.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5023, debug=True)