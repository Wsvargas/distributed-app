from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

# Configurar la clave secreta de Stripe en modo de prueba
stripe.api_key = "sk_test_51Qgbz0RmJ3SUw9yQA7S8ImE7W1jBorCNYMboIobAL179zWwl6I4F1HFXpGKSqlGLaqahc1e8OlvrgZiKmExB4O8b0068c9drd6"

@app.route('/payment', methods=['POST'])
def create_payment():
    data = request.get_json()
    amount = data.get('amount')  # Monto en centavos (ej: 1000 = $10.00 USD)

    try:
        # Crear un PaymentIntent
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            payment_method_types=['card']  # Solo aceptar tarjetas
        )

        # Devolver el client_secret para que el frontend pueda completar el pago
        return jsonify({
            "payment_intent_id": payment_intent.id,
            "client_secret": payment_intent.client_secret,
            "message": "Payment simulation initiated successfully"
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
