from flask import Flask, jsonify
from models import db_postgres, Booking
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db_postgres.init_app(app)

@app.route('/booking', methods=['GET'])
def get_booking():
    booking = Booking.query.all()
    booking_list = [{
        'id': b.id,
        'user_id': b.user_id,
        'flight_id': b.flight_id,
        'booking_date': b.booking_date,
        'status': b.status     
    } for b in booking]
    return jsonify(booking_list)

if __name__ == '__main__':
    # Create tables within the application context
    with app.app_context():
        db_postgres.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5022, debug=True)
