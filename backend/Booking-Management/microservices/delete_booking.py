from flask import Flask, jsonify
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

@app.route('/booking/<int:id>', methods=['DELETE'])
def delete_booking(id):
    booking = Booking.query.get(id)
    if not booking:
        return jsonify({'error': 'Booking not found'}), 404

    try:
        db_postgres.session.delete(booking)
        db_postgres.session.commit()
        return jsonify({'message': 'Booking deleted successfully'})
    except Exception as e:
        db_postgres.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create tables within the application context
    with app.app_context():
        db_postgres.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5024, debug=True)
