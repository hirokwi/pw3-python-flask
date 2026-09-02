<?php
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');

// Conexão com banco do Consultório Odontológico Sorriso Feliz
$conn = new mysqli("localhost", "root", "", "consultorio_odonto_db");
if ($conn->connect_error) {
    die(json_encode(["erro" => "Falha na conexão: " . $conn->connect_error]));
}

// Atualiza todas as mensagens "enviadas" para "entregue"
$conn->query("UPDATE mensagens_odonto SET status = 'entregue' WHERE status = 'enviado'");

// Busca todas as mensagens do chat com a recepção
$sql = "SELECT id, paciente, mensagem, data_hora, status FROM mensagens_odonto ORDER BY id DESC";
$result = $conn->query($sql);

$mensagens = [];
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $mensagens[] = $row;
    }
}

echo json_encode($mensagens);
$conn->close();
