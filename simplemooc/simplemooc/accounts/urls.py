import django
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from simplemooc.accounts.views import register, dashboard, edit, edit_password

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('entrar/', LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page = 'accounts:login'), name='logout'),
    path('cadastrar/', register, name='register'),
    path('editar/', edit, name='edit'),
    path('editar_senha/', edit_password, name='edit_password'),
]