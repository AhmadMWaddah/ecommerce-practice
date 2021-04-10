from django.shortcuts import render
from page.models import Showcase
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger


def not_found(request):
	context = {
		'page': 'not_found'
	}
	return render(request, 'page/not_found.html', context)


def about(request):
	context = {
		'page': 'about'
	}
	return render(request, 'page/about.html', context)


def showcases(request):
	showcases = Showcase.objects.all()
	paginator = Paginator(showcases, 4)
	page = request.GET.get('page')
	paged_showcases = paginator.get_page(page)
	context = {
		'page': 'showcases',
		'showcases': paged_showcases
	}
	return render(request, 'page/showcases.html', context)


def sitemap(request):
	context = {
		'page': 'sitemap'
	}
	return render(request, 'page/sitemap.html', context)


def privacy(request):
	context = {
		'page': 'privacy'
	}
	return render(request, 'page/privacy.html', context)


def refund(request):
	context = {
		'page': 'refund'
	}
	return render(request, 'page/refund.html', context)


def shipping(request):
	context = {
		'page': 'shipping'
	}
	return render(request, 'page/shipping.html', context)


def terms(request):
	context = {
		'page': 'terms'
	}
	return render(request, 'page/terms.html', context)