from flask import Flask, request, jsonify
import stripe
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 🔹 Permitir solicitudes desde el frontend

# 🔥 Clave secreta de Stripe (NO poner en el frontend)
stripe.api_key = "sk_test_51Qr8qUQFRejcDSxhcs6Xk2hL91atx3pAEscyPg6EzvVQgssJrZ9AK8YsKlxBYp8hbY6XTjVP0sbA88GWmh3j1TaN00DkiVEFub"

@app.route("/create-payment-intent", methods=["POST"])
def create_payment():
    try:
        data = request.get_json()
        amount = data["amount"]  # 🔹 Monto del pago (en centavos)
        currency = data["currency"]

        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"]
        )

        return jsonify({"clientSecret": intent["client_secret"]})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5005)
