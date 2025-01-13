from flask import Flask, request, jsonify
from models import db, Promotion
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/promotions', methods=['POST'])
def create_promotion():
    data = request.get_json()
    new_promotion = Promotion(
        title=data['title'],
        description=data['description'],
        discount=data['discount'],
        active=data.get('active', True)
    )
    db.session.add(new_promotion)
    db.session.commit()
    return jsonify({"message": "Promotion created successfully"}), 201

@app.route('/promotions', methods=['GET'])
def get_promotions():
    promotions = Promotion.query.all()
    result = [
        {
            "id": promo.id,
            "title": promo.title,
            "description": promo.description,
            "discount": promo.discount,
            "active": promo.active
        }
        for promo in promotions
    ]
    return jsonify(result), 200

@app.route('/promotions/<int:id>', methods=['PUT'])
def update_promotion(id):
    data = request.get_json()
    promotion = Promotion.query.get_or_404(id)
    promotion.title = data.get('title', promotion.title)
    promotion.description = data.get('description', promotion.description)
    promotion.discount = data.get('discount', promotion.discount)
    promotion.active = data.get('active', promotion.active)
    db.session.commit()
    return jsonify({"message": "Promotion updated successfully"}), 200

@app.route('/promotions/<int:id>', methods=['DELETE'])
def delete_promotion(id):
    promotion = Promotion.query.get_or_404(id)
    db.session.delete(promotion)
    db.session.commit()
    return jsonify({"message": "Promotion deleted successfully"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
