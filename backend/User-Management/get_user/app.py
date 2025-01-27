from flask import Flask, jsonify
from models import db, User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'phone': user.phone,
            'password': user.password, 
            'date_of_birth': user.date_of_birth,
            'role': user.role,
            'is_active': user.is_active
        })
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    # Create tables within the application context
    with app.app_context():
        db.create_all()
        print("Tables created successfully.")
    
    app.run(host='0.0.0.0', port=5003, debug=True)
