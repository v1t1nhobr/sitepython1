# tarefas/urls.py

from django.urls import path
from . import views

app_name = 'tarefas' 

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.dashboard_view, name='dashboard'), 
    path('logout/', views.logout_view, name='logout'),
]