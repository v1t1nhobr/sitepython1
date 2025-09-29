# MeuProjeto/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # LINHA ADICIONADA: Inclui as URLs de 'esqueceu a senha', etc.
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Sua linha existente que aponta para as URLs do app 'tarefas'
    path('', include('tarefas.urls', namespace='tarefas')),
]