from django import forms

class UploadFileForm(forms.Form):
	title = forms.charField(max_length=50)
	file  = forms.FileField()
 