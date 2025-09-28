from django.contrib import admin
from django.urls import path, include  # <-- Certifique-se de que 'include' está aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Adicione esta linha:
    # Ela diz ao Django para usar as URLs do app 'tarefas'
    path('', include('tarefas.urls', namespace='tarefas')),
]