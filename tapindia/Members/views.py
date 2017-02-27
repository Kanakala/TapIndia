from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def article_view(request, article_id):
	instance = get_object_or_404(Article, id=article_id)
	context = {
		"instance": instance,
	}
	return render(request, "loggedin_load/post_detail.html", context)