from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
    # URLs de Login/Home
    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),
    
    # Adicione a nova URL para a página de cadastro aqui
    path('cadastro/', views.cadastro_view, name='cadastro'),

    # URLs da área logada
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]