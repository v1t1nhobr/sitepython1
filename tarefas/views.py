# tarefas/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse # <-- ESTA IMPORTAÇÃO ESTAVA FALTANDO
from .models import Tarefa
from .forms import TarefaForm, CustomUserCreationForm 

# --- VIEW DE LOGIN ---
def login_view(request):
    if request.user.is_authenticated:
        return redirect('tarefas:dashboard')

    if request.method == 'POST':
        usuario_digitado = request.POST.get('username') 
        senha_digitada = request.POST.get('password')
        user = authenticate(request, username=usuario_digitado, password=senha_digitada)
        
        if user is not None:
            login(request, user)
            return redirect('tarefas:dashboard')
        else:
            context = {'error_message': 'Usuário ou senha inválidos. Tente novamente.'}
            return render(request, 'tarefas/login.html', context)
    
    return render(request, 'tarefas/login.html')

# --- VIEW DE CADASTRO ---
def cadastro_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tarefas:dashboard')
    else:
        form = CustomUserCreationForm() 
    
    context = {'form': form}
    return render(request, 'tarefas/cadastro.html', context)

# --- VIEW DA DASHBOARD---
@login_required(login_url='tarefas:login')
def dashboard_view(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            nova_tarefa = form.save(commit=False)
            nova_tarefa.usuario = request.user
            nova_tarefa.save()
            return redirect('tarefas:dashboard')
    else:
        form = TarefaForm()

    tarefas_do_usuario = Tarefa.objects.filter(usuario=request.user, concluida=False).order_by('-data_criacao')
    context = {
        'tarefas': tarefas_do_usuario,
        'form': form
    }
    return render(request, 'tarefas/dashboard.html', context)

# --- VIEW DE ATUALIZAR---
@login_required(login_url='tarefas:login')
def update_tarefa_view(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('tarefas:dashboard')
    else:
        form = TarefaForm(instance=tarefa)

    context = {'form': form, 'tarefa': tarefa}
    return render(request, 'tarefas/update_tarefa.html', context)

# --- VIEW DE DELETAR TAREFA ---
@login_required(login_url='tarefas:login')
def delete_tarefa_view(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    if request.method == 'POST':
        tarefa.delete()
    return redirect('tarefas:dashboard')

# --- VIEW DE DELETAR CONTA ---
@login_required(login_url='tarefas:login')
def delete_account_view(request):
    if request.method == 'POST':
        user = request.user
        password = request.POST.get('password')

        if user.check_password(password):
            user.delete()
            logout(request)
            return redirect('tarefas:login') 
        else:
            context = {'error_message': 'Senha incorreta. A conta não foi deletada.'}
            return render(request, 'tarefas/delete_account_confirm.html', context)

    return render(request, 'tarefas/delete_account_confirm.html')

# --- VIEW DE MARCAR/DESMARCAR TAREFA ---
@login_required(login_url='tarefas:login')
def toggle_tarefa_view(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    if request.method == 'POST':
        tarefa.concluida = not tarefa.concluida
        tarefa.save()
    return redirect('tarefas:dashboard')

# --- VIEW DE TAREFAS CONCLUÍDAS ---
@login_required(login_url='tarefas:login')
def concluidas_view(request):
    tarefas_concluidas = Tarefa.objects.filter(usuario=request.user, concluida=True).order_by('-data_criacao')
    context = {
        'tarefas': tarefas_concluidas
    }
    return render(request, 'tarefas/concluidas.html', context)

# --- VIEW DE LOGOUT ---
def logout_view(request):
    logout(request)
    return redirect('tarefas:login')

# --- MINI-API PARA BUSCAR DADOS DE UMA TAREFA ---
@login_required(login_url='tarefas:login')
def get_tarefa_json_view(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, usuario=request.user)
    data = {
        'titulo': tarefa.titulo,
        'descricao': tarefa.descricao
    }
    return JsonResponse(data)