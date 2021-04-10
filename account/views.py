from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm


def account_register(request, *args, **kwargs):
	account = request.user
	if account.is_authenticated:
		return redirect('index')
	context = {
		'page': 'register',
		'form_title': 'A.M.W Store User Register'
	}
	if request.POST:
		register_form = RegisterForm(request.POST)
		if register_form.is_valid():
			register_form.save()
			return redirect('login')
		else:
			context['register_form'] = register_form
	return render(request, 'account/register.html', context)


def account_login(request, *args, **kwargs):
	context = {
		'page': 'login',
		'form_title': 'A.M.W Store User Login'
	}
	account = request.user
	if account.is_authenticated:
		return redirect('index')

	if request.POST:
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			login_form.save()
			destination = get_redirect_if_exist(request)
			if destination:
				return redirect(destination)
			return redirect('index')
		else:
			context['login_form'] = login_form
	return render(request, 'account/login.html', context)


def get_redirect_if_exist(request):
	redirect = None
	if request.GET:
		if request.GET.get('next'):
			destination_string = request.GET.get('next')
			redirect = str(destination_string)
	return redirect


def account_logout(request):
	logout(request)
	return redirect('index')
