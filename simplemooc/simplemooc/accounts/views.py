from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset

from simplemooc.courses.models import Enrollment
User = get_user_model()

# Create your views here.

@login_required
def dashboardPageView(request):
    template_name = 'accounts/dashboard.html'
    context = {}
    context['enrollments'] = Enrollment.objects.filter(user = request.user).order_by('course')

    return render(request, template_name, context)

def registerPageView(request):
    template_name = 'accounts/register.html'
    context = {}

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            context['success'] = True
    else:
        form = RegisterForm()

    context['form'] = form
    return render(request, template_name, context)

def passwordResetPageView(request):
    template_name = 'accounts/password_reset.html'
    form = PasswordResetForm(request.POST or None)
    context = {}

    if form.is_valid():
        form.save()
        context['success'] = True

    context['form'] =  form

    return render(request, template_name, context)

def passwordResetConfirmPageView(request, key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key = key)
    form = SetPasswordForm(user=reset.user, data = request.POST or None)

    if form.is_valid():
        form.save()
        context['success'] = True

    context['form'] = form
    return render(request, template_name, context)

@login_required
def editPageView(request):
    template_name = 'accounts/edit.html'
    form = EditAccountForm()
    context = {}

    if request.method == "POST":
        form = EditAccountForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            context['color'] = 'success'
            context['message'] = 'Os dados foram alterados com sucesso!'
            return render(request, 'accounts/dashboard.html', context)
    else:
        form = EditAccountForm(instance=request.user)

    context['form'] = form
    return render(request, template_name, context)

@login_required
def editPasswordPageView(request):
    template_name = 'accounts/edit_password.html'
    context = {}

    form = PasswordChangeForm(data = request.POST or None, user = request.user)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user) #Permanece logado apos alterar a senha
        context['color'] = 'success'
        context['message'] = 'A senha foi alterada com sucesso!'
        return render(request, 'accounts/dashboard.html', context)

    context['form'] = form
    return render(request, template_name, context)
    
         