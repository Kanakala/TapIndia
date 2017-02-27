from django.shortcuts import render
from . forms import ArticleForm
from django.http import HttpResponseRedirect
import datetime



def index(request):
	return render(request, 'index.html')

def article_create(request):
	form = ArticleForm(request.POST, request.FILES )
	if form.is_valid():
		instance = form.save(commit=False)
		instance.User = request.user
		
		instance.save()
		return HttpResponseRedirect('/article_create/')
		
	else:
		form = ArticleForm()
	context = {
		"form": form,
	}
	return render(request, "article.html", context)
	
def article_view(request, article_id):
	instance = get_object_or_404(Article, id=article_id)
	context = {
		"instance": instance,
	}
	return render(request, "loggedin_load/post_detail.html", context)
	
def profile_settings(request):

	if request.method == 'POST':
		form2 = ProfileForm(request.POST, request.FILES)
		if 'interests' in request.POST:
			form1 = InterestsForm(request.POST)
			if form1.is_valid():
				instance1 = form.save(commit=False)
				instance1.User = request.user
				instance1.save()
				return HttpResponseRedirect('/profile/')
		elif 'profile' in request.POST:
			form2 = ProfileForm(request.POST, request.FILES)
			if form2.is_valid():
				instance2 = form.save(commit=False)
				instance2.User = request.user
				instance2.save()
				return HttpResponseRedirect('/profile/')
	else:
	
	form1 = InterestsForm()
	form2 = ProfileForm()
	
	instance_interests = Interests.objects.get( id = interests_id )
	if request.method == POST:
		form3 = InterestsForm( request.POST, instance = instance_interests )
		

	else:
		form1 = AcceptedForm( instance = instance_post )
	
	context = {
		"form1": form,
		"form2": form2,
		}
	return render(request, "profile_settings.html", context)
		
			
				
	
	
		