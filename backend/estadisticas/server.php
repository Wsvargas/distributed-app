<?php
require 'vendor/autoload.php';

use GraphQL\GraphQL;
use GraphQL\Type\Schema;
use GraphQL\Type\Definition\ObjectType;
use GraphQL\Type\Definition\Type;

// Configurar conexión a la base de datos MariaDB en AWS RDS
$host = 'estadisticas.ctomew44ejiz.us-east-1.rds.amazonaws.com';
$dbname = 'estadisticas';
$username = 'admin';
$password = 'password';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
} catch (PDOException $e) {
    die(json_encode(["error" => "Error de conexión a la base de datos: " . $e->getMessage()]));
}

// Definir el tipo `Reserva`
$reservaType = new ObjectType([
    'name' => 'Reserva',
    'fields' => [
        'id_reserva' => ['type' => Type::int()],
        'id_usuario' => ['type' => Type::int()],
        'id_vuelo' => ['type' => Type::int()],
        'fecha_reserva' => ['type' => Type::string()],
        'estado' => ['type' => Type::string()],
        'total_pagado' => ['type' => Type::float()],
    ],
]);

// Definir `Query`
$queryType = new ObjectType([
    'name' => 'Query',
    'fields' => [
        'reservasPorUsuario' => [
            'type' => Type::listOf($reservaType),
            'args' => [
                'id_usuario' => ['type' => Type::int()],
            ],
            'resolve' => function ($root, $args) use ($pdo) {
                $stmt = $pdo->prepare("SELECT * FROM reservas WHERE id_usuario = ?");
                $stmt->execute([$args['id_usuario']]);
                return $stmt->fetchAll();
            },
        ],
    ],
]);

// Crear esquema GraphQL
$schema = new Schema([
    'query' => $queryType,
]);

// Manejar la solicitud
try {
    $rawInput = file_get_contents('php://input');
    $input = json_decode($rawInput, true);
    $query = $input['query'] ?? '';

    $result = GraphQL::executeQuery($schema, $query);
    $output = $result->toArray();
} catch (\Exception $e) {
    $output = ['error' => $e->getMessage()];
}

// Devolver respuesta en formato JSON
header('Content-Type: application/json');
echo json_encode($output);
?>
