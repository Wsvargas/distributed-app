from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Para permitir conexiones desde el frontend
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@user-management-db.ctomew44ejiz.us-east-1.rds.amazonaws.com:5432/users_management'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    print(f"Datos recibidos: {data}")  # Esto te ayudará a depurar
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email y contraseña son requeridos"}), 400

    query = text('SELECT * FROM "user" WHERE email = :email AND password = :password')
    result = db.session.execute(query, {"email": email, "password": password}).fetchone()

    if result:
        return jsonify({"message": "Login exitoso", "user": dict(result._mapping)}), 200

    else:
        return jsonify({"message": "Usuario o contraseña incorrectos"}), 401

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
