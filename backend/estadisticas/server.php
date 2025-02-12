<?php

header("Content-Type: application/json");

// 🔹 Configuración de la base de datos MariaDB en AWS RDS
$host = "database-1.ctomew44ejiz.us-east-1.rds.amazonaws.com";
$user = "admin";
$password = "password";
$database = "estadisticas";

// 🔹 Conectar a la base de datos
$conn = new mysqli($host, $user, $password, $database);

if ($conn->connect_error) {
    die(json_encode(["error" => "Error de conexión: " . $conn->connect_error]));
}

// 🔹 Obtener datos enviados por GraphQL
$request = json_decode(file_get_contents("php://input"), true);

if (!isset($request["query"])) {
    die(json_encode(["error" => "Consulta no válida"]));
}

// 🔹 Procesar la consulta GraphQL
$query = $request["query"];

if (strpos($query, "reservasPorUsuario") !== false) {
    preg_match('/id_usuario\s*:\s*(\d+)/', $query, $matches);
    if (!isset($matches[1])) {
        die(json_encode(["error" => "Falta id_usuario"]));
    }

    $id_usuario = intval($matches[1]);
    $sql = "SELECT * FROM reservas WHERE id_usuario = $id_usuario";
    $result = $conn->query($sql);

    $reservas = [];
    while ($row = $result->fetch_assoc()) {
        $reservas[] = $row;
    }

    echo json_encode(["data" => ["reservasPorUsuario" => $reservas]]);
} else {
    echo json_encode(["error" => "Consulta no soportada"]);
}

$conn->close();
?>
