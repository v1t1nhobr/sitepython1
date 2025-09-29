# tarefas/urls.py
from django.urls import path
from . import views

app_name = 'tarefas'

# UMA ÚNICA LISTA COM TODAS AS URLS
urlpatterns = [
    # Rotas de Autenticação e Navegação Principal
    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    
    # Rotas de CRUD para Tarefas
    path('tarefa/update/<int:pk>/', views.update_tarefa_view, name='update_tarefa'),
    path('tarefa/delete/<int:pk>/', views.delete_tarefa_view, name='delete_tarefa'),
    
    # Rota da "mini-API" para buscar dados de uma tarefa
    path('api/tarefa/<int:pk>/', views.get_tarefa_json_view, name='get_tarefa_json'),
    
    path('delete_account/', views.delete_account_view, name='delete_account'),
]