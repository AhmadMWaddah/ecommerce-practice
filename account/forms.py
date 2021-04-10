from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Account


class RegisterForm(UserCreationForm):
	email = forms.EmailField(max_length=250, help_text='Must Be Valid E-Mail.')

	class Meta:
		model = Account
		fields = ('email', 'username', 'password1', 'password2')

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = Account.objects.get(email=email)
		except Exception as e:
			return email
		raise forms.ValidationError(f'E-Mail {email} Is Already Exists.')

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.get(username=username)
		except Exception as e:
			return username
		raise forms.ValidationError(f'Username {username} Is Already Exists.')


class LoginForm(forms.ModelForm):
	password = forms.CharField(label='password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def save(self):
		email = self.cleaned_data['email']
		password = self.cleaned_data['password']
		account = authenticate(email=email, password=password)
		if account:
			login(request, account)