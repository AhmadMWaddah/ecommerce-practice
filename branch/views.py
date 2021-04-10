from django.shortcuts import render
from branch.models import Branch


def branch(request):
	branches = Branch.objects.all()
	context = {
		'page': 'branch',
		'branches': branches,
	}
	return render(request, 'branch/branch.html', context)
