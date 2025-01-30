from flask import Flask, request, jsonify
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

@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    
    if not nombre and not email:
        return jsonify({'error': 'Se requiere al menos un campo para actualizar (nombre o email).'}), 400

    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'error': 'Usuario no encontrado.'}), 404

    try:
        if nombre:
            usuario.nombre = nombre
        if email:
            usuario.email = email
        
        db.session.commit()
        return jsonify({'message': 'Usuario actualizado exitosamente'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Crear tablas dentro del contexto de la aplicación (si es necesario)
    with app.app_context():
        db.create_all()
        print("Tablas creadas exitosamente.")
    
    app.run(host='0.0.0.0', port=5008, debug=True)
