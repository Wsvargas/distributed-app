from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# PostgreSQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/users_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model with additional characteristics
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(200), nullable=False)  # Hashed password
    date_of_birth = db.Column(db.Date, nullable=True)
    role = db.Column(db.String(50), nullable=False, default='user')
    is_active = db.Column(db.Boolean, default=True)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')
    date_of_birth = data.get('date_of_birth')
    role = data.get('role', 'user')  # Default to 'user' if no role is provided
    is_active = data.get('is_active', True)  # Default to True if no value provided

    if not name or not email or not password:
        return jsonify({'error': 'Name, email, and password are required'}), 400

    # Create a new user instance
    new_user = User(
        name=name,
        email=email,
        phone=phone,
        password=password,  # You should hash this before storing in production
        date_of_birth=date_of_birth,
        role=role,
        is_active=is_active
    )

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create tables within the application context
    with app.app_context():
        db.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5001, debug=True)