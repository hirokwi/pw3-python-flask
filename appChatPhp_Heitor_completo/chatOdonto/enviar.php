<?php
header("Access-Control-Allow-Origin: http://localhost:8081");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization");
header("Content-Type: application/json; charset=UTF-8");

// Conexão com banco do Consultório Odontológico Sorriso Feliz
$conn = new mysqli("localhost", "root", "", "consultorio_odonto_db");
if ($conn->connect_error) {
    die(json_encode(["erro" => "Falha na conexão: " . $conn->connect_error]));
}

// Pega JSON enviado pelo React Native
$input = json_decode(file_get_contents("php://input"), true);
$paciente = $conn->real_escape_string($input['paciente']);
$mensagem = $conn->real_escape_string($input['mensagem']);

// Insere mensagem do paciente no banco (tabela mensagens_odonto)
$sql = "INSERT INTO mensagens_odonto (paciente, mensagem, status) VALUES ('$paciente', '$mensagem', 'enviado')";
if ($conn->query($sql) === TRUE) {
    echo json_encode(["sucesso" => true, "id" => $conn->insert_id]);
} else {
    echo json_encode(["erro" => "Erro ao salvar mensagem: " . $conn->error]);
}

$conn->close();
