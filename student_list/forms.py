from django import forms
from .models import List
	
class ListForm(forms.ModelForm):
	class Meta:
		model = List
		fields = ['lastname', 'firstname', 'yearlevel', 'course', 'gender']

class EditForm(forms.ModelForm):
	class Meta:
		model = List
		fields = ['lastname', 'firstname', 'yearlevel', 'course', 'gender']