from django.contrib.auth.forms import UserCreationForm
from .models import Account, MyAccountManager


class FormRegister(UserCreationForm):

	class Meta:
		model = Account
		fields = ['email', 'username', 'location', 'first_name', 'last_name', 'username', 'mobile', 'password1', 'password2']

