from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

# MariaDB Database Configuration
app.config['MYSQL_HOST'] = 'db'  # Change to the address of your MariaDB server
app.config['MYSQL_USER'] = 'root'  # MariaDB username
app.config['MYSQL_PASSWORD'] = 'password'  # MariaDB password
app.config['MYSQL_DB'] = 'flights_management'  # Database name
mysql = MySQL(app)

# Flight model (simplified version)
class Flight:
    def __init__(self, flight_number, origin, destination, departure_date, arrival_date, status, airline, is_active=True):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_date = datetime.strptime(departure_date, '%Y-%m-%d %H:%M:%S')
        self.arrival_date = datetime.strptime(arrival_date, '%Y-%m-%d %H:%M:%S')
        self.status = status
        self.airline = airline
        self.is_active = is_active

# DELETE route for removing a flight by ID
@app.route('/flights/<int:id>', methods=['DELETE'])
def delete_flight(id):
    try:
        cursor = mysql.connection.cursor()
        
        # Check if the flight exists
        cursor.execute("SELECT * FROM flights WHERE id = %s", (id,))
        flight = cursor.fetchone()
        
        if not flight:
            return jsonify({'error': 'Flight not found'}), 404
        
        # Delete the flight
        cursor.execute("DELETE FROM flights WHERE id = %s", (id,))
        mysql.connection.commit()
        
        cursor.close()
        return jsonify({'message': 'Flight deleted successfully'}), 200
    except Exception as e:
        mysql.connection.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create tables in the database if they don't exist
    with app.app_context():
        cursor = mysql.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS flights (
                id INT AUTO_INCREMENT PRIMARY KEY,
                flight_number VARCHAR(100) NOT NULL UNIQUE,
                origin VARCHAR(100) NOT NULL,
                destination VARCHAR(100) NOT NULL,
                departure_date DATETIME NOT NULL,
                arrival_date DATETIME NOT NULL,
                status VARCHAR(50) NOT NULL,
                airline VARCHAR(100) NOT NULL,
                is_active BOOLEAN DEFAULT TRUE
            );
        """)
        mysql.connection.commit()
        cursor.close()

    app.run(host='0.0.0.0', port=5014, debug=True) 