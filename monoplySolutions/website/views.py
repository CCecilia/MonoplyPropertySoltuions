from django.shortcuts import render

def index(request):
	# dec vars

	context = {
		'page': 'index'
	}

	return render(request, 'index.html', context)
