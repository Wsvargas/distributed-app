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

# 1. Update flight (PUT)
@app.route('/flights/<int:id>', methods=['PUT'])
def update_flight(id):
    data = request.get_json()
    
    flight_number = data.get('flight_number')
    origin = data.get('origin')
    destination = data.get('destination')
    departure_date = data.get('departure_date')
    arrival_date = data.get('arrival_date')
    status = data.get('status')
    airline = data.get('airline')
    is_active = data.get('is_active')

    # Ensure at least one field is provided for update
    if not any([flight_number, origin, destination, departure_date, arrival_date, status, airline, is_active is not None]):
        return jsonify({'error': 'At least one field (flight_number, origin, destination, departure_date, arrival_date, status, airline, is_active) is required for update.'}), 400

    cursor = mysql.connection.cursor()
    
    # Check if the flight exists
    cursor.execute("SELECT * FROM flights WHERE id = %s", (id,))
    flight = cursor.fetchone()
    
    if not flight:
        cursor.close()
        return jsonify({'error': 'Flight not found.'}), 404

    try:
        if flight_number:
            cursor.execute("UPDATE flights SET flight_number = %s WHERE id = %s", (flight_number, id))
        if origin:
            cursor.execute("UPDATE flights SET origin = %s WHERE id = %s", (origin, id))
        if destination:
            cursor.execute("UPDATE flights SET destination = %s WHERE id = %s", (destination, id))
        if departure_date:
            cursor.execute("UPDATE flights SET departure_date = %s WHERE id = %s", (datetime.strptime(departure_date, '%Y-%m-%d %H:%M:%S'), id))
        if arrival_date:
            cursor.execute("UPDATE flights SET arrival_date = %s WHERE id = %s", (datetime.strptime(arrival_date, '%Y-%m-%d %H:%M:%S'), id))
        if status:
            cursor.execute("UPDATE flights SET status = %s WHERE id = %s", (status, id))
        if airline:
            cursor.execute("UPDATE flights SET airline = %s WHERE id = %s", (airline, id))
        if is_active is not None:
            cursor.execute("UPDATE flights SET is_active = %s WHERE id = %s", (is_active, id))
        
        mysql.connection.commit()
        cursor.close()
        return jsonify({'message': 'Flight updated successfully.'}), 200
    except Exception as e:
        mysql.connection.rollback()
        cursor.close()
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

    app.run(host='0.0.0.0', port=5013, debug=True)