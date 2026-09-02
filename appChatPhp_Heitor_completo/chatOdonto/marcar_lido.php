<?php
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');

// Conexão com banco do Consultório Odontológico Sorriso Feliz
$conn = new mysqli("localhost", "root", "", "consultorio_odonto_db");
if ($conn->connect_error) {
    die(json_encode(["erro" => "Falha na conexão: " . $conn->connect_error]));
}

$input = json_decode(file_get_contents("php://input"), true);
$paciente = $conn->real_escape_string($input['paciente']);

// Marca como lida toda mensagem que não seja do próprio paciente que está com o app aberto
$sql = "UPDATE mensagens_odonto SET status = 'lido' WHERE paciente != '$paciente' AND status = 'entregue'";
$conn->query($sql);

echo json_encode(["sucesso" => true]);
$conn->close();
