from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from simplemooc.accounts.views import registerPageView, dashboardPageView, editPageView, editPasswordPageView, passwordResetPageView, passwordResetConfirmPageView

urlpatterns = [
    path('', dashboardPageView, name='dashboard'),
    path('entrar/', LoginView.as_view(template_name = 'accounts/login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page = 'accounts:login'), name='logout'),
    path('cadastrar/', registerPageView, name='register'),
    path('esqueceu_senha/', passwordResetPageView, name='password_reset'),
    path('alterar_senha/<str:key>', passwordResetConfirmPageView, name='password_reset_confirm'),
    path('editar/', editPageView, name='edit'),
    path('editar_senha/', editPasswordPageView, name='edit_password'),
]