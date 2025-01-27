from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# PostgreSQL database configuration (actualizada a db_postgres)
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

@app.route('/bookings/<int:id>', methods=['GET'])
def get_booking(id):
    booking = Booking.query.get(id)
    if booking:
        return jsonify({
            'id': booking.id,
            'user_id': booking.user_id,
            'flight_id': booking.flight_id,
            'booking_date': booking.booking_date.strftime('%Y-%m-%dT%H:%M:%S'),
            'status': booking.status
        })
    return jsonify({'error': 'Booking not found'}), 404

if __name__ == '__main__':
    # Create tables within the application context
    with app.app_context():
        db_postgres.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5022, debug=True)
