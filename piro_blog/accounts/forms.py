from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class AuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Your id or password is wrong',
        'inactive': 'No user',
    }


class SignupForm(UserCreationForm):
    error_messages = {
        'password_mismatch': 'wrong password',
    }

    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is None and email.split('@')[1] != 'sju.ac.kr':
            raise forms.VaildationError('Only sju mail !')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # 여기서 commit=True 된다.
        if commit:
            user.save()
        return user


class SignUpProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'image', )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
