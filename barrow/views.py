from django.shortcuts import render


def view_barrow(request):
	context = {
		'page': 'barrow',
		'msg': 'This Page is Not Functional, and Will be in the Coming Steps.'
	}
	return render(request, 'barrow/barrow.html', context)


def add_to_barrow(request):
	context = {
		'page': 'add_to_barrow',
		'msg': 'This Page is Not Functional, and Will be in the Coming Steps.'
	}
	return render(request, 'barrow/add_to_barrow.html', context)


def remove_from_barrow(request):
	context = {
		'page': 'remove_from_barrow',
		'msg': 'This Page is Not Functional, and Will be in the Coming Steps.'
	}
	return render(request, 'barrow/remove_from_barrow.html', context)


def clear_barrow(request):
	context = {
		'page': 'clear_barrow',
		'msg': 'This Page is Not Functional, and Will be in the Coming Steps.'
	}
	return render(request, 'barrow/clear_barrow.html', context)
