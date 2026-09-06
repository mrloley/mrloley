from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Registra um novo usuário."""
    if request.method != 'POST':
        # Exibe formulário de registro em branco.
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Faz login do usuário e redireciona para a página inicial.
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)