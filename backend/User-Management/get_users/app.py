from flask import Flask, jsonify
from models import db, User
from config import Config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{
        'id': u.id,
        'name': u.name,
        'email': u.email,
        'phone': u.phone,
        'password': u.password,  # Ensure this is hashed in production
        'date_of_birth': u.date_of_birth,
        'role': u.role,
        'is_active': u.is_active
    } for u in users]
    return jsonify(users_list)

if __name__ == '__main__':
    # Create tables within the application context
    with app.app_context():
        db.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5002, debug=True)
