from django.contrib import admin
from django.db import models
from .models import Article


class ArticleModelAdmin(admin.ModelAdmin):
	list_display = ["TimeStamp", "Category", "Headline", "Body", "Notes", ]
	list_display_links = ["Category",]
	list_editable = [ "Headline", "Body", "Notes",]
	list_filter = ["TimeStamp", "Category", ]

	search_fields = ["Category", "Headline",]
	class Meta:
		model = Article

admin.site.register( Article, ArticleModelAdmin)

