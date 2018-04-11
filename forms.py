from django import forms
from myapp.models import Data ,data2
from myapp.models import Publisher
from django.forms import TextInput,Textarea
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from tinymce.widgets import TinyMCE

class MyloginForm(forms.Form):
	first_name = forms.CharField(label='First Name',max_length=30)
	last_name = forms.CharField(label=' Last Name',max_length=30)
	

class data2Form(forms.ModelForm):
	description = forms.CharField(widget=TinyMCE(attrs={'cols':80,'rows':30}))
	
		
	#class Meta : 
	#	model = data2
	#	exclude = ()

class publisher_form(forms.ModelForm):
	name = forms.CharField(max_length=30)
	address = forms.CharField(max_length=50)
	mobile = forms.CharField(max_length=10)
	city = forms.CharField(max_length=60)
	state_province = forms.CharField(max_length=20)
	country = forms.CharField(max_length=20)
	website = forms.URLField()
