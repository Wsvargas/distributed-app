from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/gestion_usuarios'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        return jsonify({'id': usuario.id, 'nombre': usuario.nombre, 'email': usuario.email})
    return jsonify({'error': 'Usuario no encontrado'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
