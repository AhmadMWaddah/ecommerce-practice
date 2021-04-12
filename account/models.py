from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('E-Mail Address Required.')

		account = self.model(
			email=self.normalize_email(email),
		)
		account.set_password(password)
		account.save(using=self._db)
		return account

	def create_superuser(self, email, password):
		account = self.create_user(
			email=self.normalize_email(email),
			password=password
		)
		account.is_admin = True
		account.is_staff = True
		account.is_superuser = True
		account.save(using=self._db)
		return account


def account_image_path(self):
	return f'accounts/{self.account_id}/{"account_image.png"}'


def default_account_image():
	return 'default/default_account_image.png'


class Account(AbstractBaseUser):
	class Meta:
		ordering = ['email']
		verbose_name = 'Account'
		verbose_name_plural = 'Accounts'

	account_id = models.AutoField(verbose_name='ID', primary_key=True)
	email = models.EmailField(verbose_name='E-Mail', max_length=60, unique=True)
	username = models.CharField(verbose_name='Username', max_length=60, blank=True, null=True)
	first_name = models.CharField(verbose_name='First Name', max_length=30, blank=True, null=True)
	last_name = models.CharField(verbose_name='Last Name', max_length=30, blank=True, null=True)
	age = models.IntegerField(verbose_name='Age', blank=True, null=True)
	mobile = models.CharField(verbose_name='Mobile', max_length=15, blank=True, null=True)
	location = models.CharField(verbose_name='Location', max_length=255, blank=True, null=True)
	date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)
	is_active = models.BooleanField(verbose_name='Is Active', default=True)
	is_superuser = models.BooleanField(verbose_name='Is Superuser', default=False)
	is_staff = models.BooleanField(verbose_name='Is Staff', default=False)
	is_admin = models.BooleanField(verbose_name='Is Admin', default=False)
	image = models.ImageField(verbose_name='Image', null=True, blank=True, upload_to=account_image_path, default=default_account_image)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = MyAccountManager()

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True
