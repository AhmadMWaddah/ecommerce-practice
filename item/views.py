from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from item.models import Item
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger


def items(request):
	items = Item.objects.all()
	paginator = Paginator(items, 4)
	page = request.GET.get('page')
	paged_items = paginator.get_page(page)
	context = {
		'page': 'items',
		'items': paged_items,
	}
	return render(request, 'item/items.html', context)


def item(request, itm_sku):
	item = get_object_or_404(Item, itm_sku=itm_sku)
	related_items = Item.objects.all().filter(itm_ctgry=item.itm_ctgry)
	context = {
		'page': 'item',
		'item': item,
		'related_items': related_items
	}
	return render(request, 'item/item.html', context)


def item_search(request):
	if request.method == 'POST':
		searched_item = get_object_or_404(
			Q(itm_sku__icontains=request.data) | Q(itm_nme__icontains=request.data) | Q(itm_desc__icontains=request.data)
		)
	if not searched_item:
		return render(request, 'page/not_found.html')
	else:
		context = {
			'searched_item': searched_item,
		}
		return render(request, 'item/item_search.html', context)