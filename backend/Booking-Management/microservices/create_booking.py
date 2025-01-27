from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# PostgreSQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db_postgres:5432/booking_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_postgres = SQLAlchemy(app)

# Booking model
class Booking(db_postgres.Model):
    id = db_postgres.Column(db_postgres.Integer, primary_key=True)
    user_id = db_postgres.Column(db_postgres.Integer, nullable=False)
    flight_id = db_postgres.Column(db_postgres.Integer, nullable=False)
    booking_date = db_postgres.Column(db_postgres.DateTime, nullable=False)
    status = db_postgres.Column(db_postgres.String(50), nullable=False)

@app.route('/booking', methods=['POST'])
def create_booking():
    data = request.get_json()
    user_id = data.get('user_id')
    flight_id = data.get('flight_id')
    booking_date = data.get('booking_date')
    status = data.get('status', 'pending')  # Default to 'pending' if no status is provided

    # Validate required fields
    if not user_id or not flight_id or not booking_date:
        return jsonify({'error': 'User ID, flight ID, and booking date are required'}), 400

    try:
        # Convert booking_date string to datetime object
        booking_date = datetime.strptime(booking_date, '%Y-%m-%dT%H:%M:%S')

        # Create a new booking instance
        new_booking = Booking(
            user_id=user_id,
            flight_id=flight_id,
            booking_date=booking_date,
            status=status
        )

        db_postgres.session.add(new_booking)
        db_postgres.session.commit()
        return jsonify({'message': 'Booking created successfully'}), 201
    except Exception as e:
        db_postgres.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create tables within the application context
    with app.app_context():
        db_postgres.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5021, debug=True)
