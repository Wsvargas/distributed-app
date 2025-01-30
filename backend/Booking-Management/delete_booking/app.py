from flask import Flask, jsonify
from models import db_postgres, Booking
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db_postgres.init_app(app)

@app.route('/booking/<int:id>', methods=['DELETE'])
def delete_booking(id):
    booking = Booking.query.get(id)
    if not booking:
        return jsonify({'error': 'Booking not found'}), 404

    try:
        db_postgres.session.delete(booking)
        db_postgres.session.commit()
        return jsonify({'message': 'Booking deleted successfully'}), 200
    except Exception as e:
        db_postgres.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create tables within the application context
    with app.app_context():
        db_postgres.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5024, debug=True)
