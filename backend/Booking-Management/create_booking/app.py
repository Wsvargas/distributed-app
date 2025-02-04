<<<<<<< HEAD
from flask import Flask, request, jsonify
from config import Config
from models import db_postgres, Booking
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db_postgres.init_app(app)

@app.route('/booking', methods=['POST'])
def create_booking():
    data = request.get_json()
    user_id = data.get('user_id')
    flight_id = data.get('flight_id')
    booking_date = data.get('booking_date')
    status = data.get('status', 'pending')  # Default to 'pending' if not provided

    # Validate required fields
    if not user_id or not flight_id or not booking_date:
        return jsonify({'error': 'User ID, flight ID, and booking date are required'}), 400

    try:
        # Parse booking_date string to datetime
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
    with app.app_context():
        db_postgres.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5021, debug=True)
=======
from flask import Flask, request, jsonify
from config import Config
from models import db_postgres, Booking
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db_postgres.init_app(app)

@app.route('/booking', methods=['POST'])
def create_booking():
    data = request.get_json()
    user_id = data.get('user_id')
    flight_id = data.get('flight_id')
    booking_date = data.get('booking_date')
    status = data.get('status', 'pending')  # Default to 'pending' if not provided

    # Validate required fields
    if not user_id or not flight_id or not booking_date:
        return jsonify({'error': 'User ID, flight ID, and booking date are required'}), 400

    try:
        # Parse booking_date string to datetime
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
    with app.app_context():
        db_postgres.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5021, debug=True)
>>>>>>> origin/WILLIAN
