from django import forms
from . models import Article, Interests, Profile
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class ArticleForm(forms.ModelForm):
	Category = forms.CharField(max_length=50, label = 'Category')
	Headline = forms.CharField(max_length=100, label = 'Your Article Headline Goes Here...')
	Body = forms.CharField(widget=SummernoteWidget(attrs={'width': '100%', 'height': '400px'}))
	Notes = forms.CharField(max_length=100, label = 'What problem/news/opinion are you discussing? Summarise your article in three points')
	
	class Meta:
		model = Article
		fields = ['Category', 'Headline', 'Body', 'Notes', 'Confirm']
		
class InterestsForm(forms.ModelForm):
	Regions = (
        ('North', 'North'),
        ('East', 'East'),
        ('South', 'South'),
        ('West', 'West'),
		('Central', 'Central'),
    )
	Region = forms.MultipleChoiceField(choices=Regions, widget=forms.CheckboxSelectMultiple())
	
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
	Company = forms.MultipleChoiceField(choices=Companies, widget=forms.CheckboxSelectMultiple())
	
	Markets = (
        ('Equity', 'Equity'),
        ('Commodities', 'Commodities'),
        ('Currencies', 'Currencies'),
        ('Fixed Income', 'Fixed Income'),
		('Global Economies', 'Global Economies'),
		('Mergers & Acquisitions', 'Mergers & Acquisitions'),
    )
	
	Market = forms.MultipleChoiceField(choices=Markets, widget=forms.CheckboxSelectMultiple())
	
	Politics = forms.ChoiceField(widget=forms.RadioSelect())
	Startups = forms.ChoiceField(widget=forms.RadioSelect())
	
	class Meta:
		model = "Interests",
		fields = ['Region', 'Company', 'Market', 'Politics', 'Startups',]
		
class ProfileForm(forms.ModelForm):

	Full_Name = forms.CharField()
	About = forms.CharField()
	Profile_Pic = forms.ImageField()
	
	class meta:
		model = "Profile",
		fields = ['Full_Name', 'About', 'Profile_Pic',]
		

		
