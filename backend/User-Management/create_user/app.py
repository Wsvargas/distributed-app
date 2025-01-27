from flask import Flask, request, jsonify
from models import db, User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

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
