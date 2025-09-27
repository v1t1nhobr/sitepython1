<?php

// 1. Verifica se o formulário foi enviado usando o método POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    // 2. Recebe e limpa os dados do formulário
    // Usamos 'htmlspecialchars' e 'trim' para segurança básica
    $email = htmlspecialchars(trim($_POST['email']));
    $senha = htmlspecialchars(trim($_POST['senha']));

    // 3. Validação básica (verifica se os campos não estão vazios)
    if (empty($email) || empty($senha)) {
        // Se estiver vazio, exibe uma mensagem de erro
        die("Erro: Por favor, preencha todos os campos.");
    }
    
    // --- SIMULAÇÃO DE VERIFICAÇÃO DE LOGIN ---
    
    // ATENÇÃO: Em um projeto real, você faria a conexão com o banco de dados
    // e verificaria se o E-mail e a SENHA (com hash) correspondem a um registro.
    
    // Exemplo de credenciais válidas (apenas para teste)
    $email_correto = "teste@exemplo.com";
    $senha_correta = "123456"; // Nunca armazene senhas assim em um projeto real!

    // 4. Verifica as credenciais
    if ($email === $email_correto && $senha === $senha_correta) {
        // Se as credenciais estiverem corretas:
        
        // **PARABÉNS! LOGIN BEM-SUCEDIDO!**
        
        // Inicia a sessão (para manter o usuário logado)
        session_start();
        
        // Define variáveis de sessão
        $_SESSION['logado'] = true;
        $_SESSION['email_usuario'] = $email;
        
        // Redireciona o usuário para a página de perfil/dashboard
        header("Location: dashboard.php");
        exit;
        
    } else {
        // Se as credenciais estiverem incorretas:
        echo "Erro de Login: Email ou senha inválidos.";
        
        // Você pode redirecionar para a página de login com um erro:
        // header("Location: index.html?erro=1");
        // exit;
    }
    
} else {
    // Se a página for acessada diretamente (sem envio de formulário)
    echo "Acesso inválido. Por favor, use o formulário de login.";
}

?>