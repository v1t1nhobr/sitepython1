<?php
// 1. Inicia a sessão
session_start();

// 2. Verifica se o usuário está logado
if (!isset($_SESSION['logado']) || $_SESSION['logado'] !== true) {
    // Se não estiver logado, redireciona para a tela de login
    header("Location: Login Python/login.html");
    exit; // Importante para parar a execução do script
}

// Opcional: Pegar o nome/email do usuário logado para personalização
$email_usuario = $_SESSION['email_usuario'] ?? 'Usuário';

// Se o script chegou até aqui, o usuário está logado e o HTML será exibido.
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="cssdosite.css">
  <link rel="shortcut icon" href="img/TASKO.ico" type="image/x-icon">
  <title>Tasko - Dashboard</title>
</head>
<body>
  <header>
    <div style="text-align: right;">
            <button class="login"><a href="logout.php">👤 SAIR</a> </button>
    </div>
  </header>

  <div class="container">
    <aside class="sidebar">
      <nav>