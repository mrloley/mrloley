"""Define padrões de URL para users."""

from django.urls import path, include

from . import views


app_name = 'users'
urlpatterns = [
    # Incluir URLs de autenticação padrão do Django.
    path('', include('django.contrib.auth.urls')),
    # Página de registro
    path('register/', views.register, name='register'),
]