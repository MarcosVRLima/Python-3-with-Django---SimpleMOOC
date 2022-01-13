from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import PasswordInput

from simplemooc.core.mail import send_mail_template
from simplemooc.core.utils import generated_hash_key

from .models import PasswordReset

User = get_user_model()

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        else:
            raise forms.ValidationError('Nenhum usuário encontrado com este e-mails')

    def save(self):
        user = User.objects.get(email = self.cleaned_data['email'])
        key = generated_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'accounts/password_reset_email.html'

        #mail
        subject = 'Criar nova senha do SimpleMOOC!'
        context = {'reset': reset,}
        send_mail_template(subject, template_name, context, [user.email])

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label = 'Senha', widget=PasswordInput)
    password2 = forms.CharField(label = 'Confirme sua senha', widget=PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas são diferentes')

        return password2

    def save(self, commit: True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()

        return user
    
    class Meta:
        model = User
        fields = ['username', 'email']

class EditAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name']
