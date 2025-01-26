<?php
require 'vendor/autoload.php';

use Stripe\Stripe;
use Stripe\PaymentIntent;

// Configurar la clave secreta de Stripe
Stripe::setApiKey('sk_test_51Qgbz0RmJ3SUw9yQA7S8ImE7W1jBorCNYMboIobAL179zWwl6I4F1HFXpGKSqlGLaqahc1e8OlvrgZiKmExB4O8b0068c9drd6');

header('Content-Type: application/json');

// Manejar la solicitud de creación de un pago
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = json_decode(file_get_contents('php://input'), true);
    $amount = $input['amount'];  // Monto en centavos (ej: 1000 = $10.00)

    try {
        // Crear un PaymentIntent en Stripe
        $paymentIntent = PaymentIntent::create([
            'amount' => $amount,
            'currency' => 'usd',
            'payment_method_types' => ['card'],
        ]);

        echo json_encode([
            'clientSecret' => $paymentIntent->client_secret,
            'message' => 'Payment initiated successfully'
        ]);
    } catch (Exception $e) {
        http_response_code(500);
        echo json_encode(['error' => $e->getMessage()]);
    }
}
?>
