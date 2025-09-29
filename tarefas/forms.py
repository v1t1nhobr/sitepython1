# tarefas/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'O que precisa ser feito?'}),
            'descricao': forms.Textarea(attrs={'placeholder': 'Adicione uma descrição...', 'rows': 4}),
        }
        labels = {
            'titulo': '',
            'descricao': ''
        }

# --- FORMULÁRIO DE CADASTRO CUSTOMIZADO E TRADUZIDO ---
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Traduzindo o campo de nome de usuário
        self.fields['username'].label = "Nome de usuário"
        self.fields['username'].help_text = "Obrigatório. 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas."

        # limpamos o help_text automático dos campos de senha
        self.fields['password1'].label = "Senha"
        self.fields['password1'].help_text = None # Remove o texto de ajuda padrão
        
        self.fields['password2'].label = "Confirmação de senha"
        self.fields['password2'].help_text = None # Remove o texto de ajuda padrão

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username",)