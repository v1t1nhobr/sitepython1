# tarefas/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm  # <-- 1. IMPORTAÇÃO NOVA
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# A função de login que o urls.py está procurando:
def login_view(request):
    """Processa o formulário de login."""
    # Se o usuário já está logado, redireciona para a dashboard
    if request.user.is_authenticated:
        return redirect('tarefas:dashboard')

    if request.method == 'POST':
        # Esta parte é crucial: pega os dados do formulário e tenta autenticar
        usuario_digitado = request.POST.get('username') 
        senha_digitada = request.POST.get('password')
        
        user = authenticate(request, username=usuario_digitado, password=senha_digitada)
        
        if user is not None:
            login(request, user)
            return redirect('tarefas:dashboard')
        else:
            # Mensagem de erro se a autenticação falhar
            context = {'error_message': 'Usuário ou senha inválidos. Tente novamente.'}
            return render(request, 'tarefas/login.html', context)
    
    # Exibe o formulário de login (login.html)
    return render(request, 'tarefas/login.html')


# A função de dashboard que o urls.py está procurando:
@login_required(login_url='tarefas:login') # Protege a página: só acessível após login
def dashboard_view(request):
    """Página da Dashboard - A área restrita."""
    # O HTML da Dashboard será renderizado
    return render(request, 'tarefas/dashboard.html')


# A função de logout que o urls.py está procurando:
def logout_view(request):
    """Desloga o usuário e redireciona para a página de login."""
    logout(request)
    return redirect('tarefas:login')


# 2. NOVA FUNÇÃO DE CADASTRO
def cadastro_view(request):
    """Processa o formulário de criação de nova conta."""
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados enviados
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Se o formulário for válido, salva o novo usuário no banco de dados
            user = form.save()
            # Loga o usuário recém-criado automaticamente
            login(request, user)
            # Redireciona para a dashboard
            return redirect('tarefas:dashboard')
    else:
        # Se for um GET, apenas cria uma instância do formulário vazio
        form = UserCreationForm()
    
    # Prepara o contexto para enviar o formulário para o template
    context = {'form': form}
    # Renderiza a página de cadastro com o formulário
    return render(request, 'tarefas/cadastro.html', context)