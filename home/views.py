from django.shortcuts import render
from page.models import Showcase


def index(request):
	showcases = Showcase.objects.all()
	showcase1 = showcases.first()
	showcase2 = showcases.last()
	context = {
		'page': 'home',
		"showcase1": showcase1,
		'showcase2': showcase2
	}
	return render(request, 'index.html', context)
