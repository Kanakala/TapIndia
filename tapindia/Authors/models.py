from django.db import models
from django.conf import settings

class Article(models.Model):
	
	User = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	Category = models.CharField(max_length=50)
	Headline = models.CharField(max_length=100)
	Body = models.TextField(max_length=10000000)
	Notes = models.CharField(max_length=100)
	Confirm = models.BooleanField()
	TimeStamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	
class Interests(models.Model):

	User = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	Regions = (
        ('North', 'North'),
        ('East', 'East'),
        ('South', 'South'),
        ('West', 'West'),
		('Central', 'Central'),
    )
	Region = models.CharField(max_length=200, choices=Regions)
	
	Companies = (
        ('Energy', 'Energy'),
        ('Financials', 'Financials'),
        ('Industrials', 'Industrials'),
        ('Health', 'Health'),
		('Media', 'Media'),
		('Retail & Consumer', 'Retail & Consumer'),
        ('Technology', 'Technology'),
        ('Telecoms', 'Telecoms'),
		('Transport', 'Transport'),
    )
	Company = models.CharField(max_length=200, choices=Companies)
	
	Markets = (
        ('Equity', 'Equity'),
        ('Commodities', 'Commodities'),
        ('Currencies', 'Currencies'),
        ('Fixed Income', 'Fixed Income'),
		('Global Economies', 'Global Economies'),
		('Mergers & Acquisitions', 'Mergers & Acquisitions'),
    )
	
	Market = models.CharField(max_length=200, choices=Markets)
	
	Politics = models.CharField(max_length=30)
	Startups = models.CharField(max_length=30)
	
class Profile(models.Model):
	
	User = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	Full_Name = models.CharField(max_length=50)
	About = models.CharField(max_length=1000)
	Profile_Pic = models.ImageField(upload_to='profile_picture/', blank=True, null=True)
	
	
	
	
	