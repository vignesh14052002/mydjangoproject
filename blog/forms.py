from django import forms
from .models import Image


class ImageForm(forms.Form,forms.ModelForm):
	name= forms.CharField(label="Name",max_length=200)
	class Meta:
		model = Image
		fields = ('name','image')
class CreateNewList(forms.Form):
	name= forms.CharField(label="Name",max_length=200)
	check=forms.BooleanField()