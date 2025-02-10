from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from models import db_postgres, Flight

app = Flask(__name__)
app.config.from_object(Config)
db_postgres.init_app(app)
CORS(app)

@app.route('/flights/<int:id>', methods=['DELETE'])
def delete_flight(id):
    flight = Flight.query.get(id)
    if not flight:
        return jsonify({"message": "Flight not found"}), 404

    try:
        db_postgres.session.delete(flight)
        db_postgres.session.commit()
        return jsonify({"message": "Flight deleted successfully"}), 200
    except Exception as e:
        db_postgres.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5035, debug=True)
