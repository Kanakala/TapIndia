from django.conf.urls import  url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^article_create/$', views.article_create, name='article_create'),
	url(r'^$', views.article_view, name='article_view'),
	] 
	
