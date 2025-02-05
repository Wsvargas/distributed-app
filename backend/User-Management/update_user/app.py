from flask import Flask, request, jsonify
from models import db, User
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    password = data.get('password')
    date_of_birth = data.get('date_of_birth')
    role = data.get('role')
    is_active = data.get('is_active')

    # Ensure at least one field is provided for update
    if not any([name, email, phone, password, date_of_birth, role, is_active is not None]):
        return jsonify({'error': 'At least one field (name, email, phone, password, date_of_birth, role, is_active) is required for update.'}), 400

    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    try:
        if name:
            user.name = name
        if email:
            user.email = email
        if phone:
            user.phone = phone
        if password:
            user.password = password  # Hash the password before saving in production
        if date_of_birth:
            user.date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d').date()  # Ensure correct date format
        if role:
            user.role = role
        if is_active is not None:
            user.is_active = is_active
        
        db.session.commit()
        return jsonify({'message': 'User updated successfully.'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5008, debug=True)