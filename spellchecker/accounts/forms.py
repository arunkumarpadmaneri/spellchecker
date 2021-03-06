from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Profile

# class ProfileForm(forms.ModelForm):
#     dob = forms.DateField(required=False, input_formats='%d/%m/%y')
#     class Meta:
#         model = Profile
#         fields = ('dob', 'location')

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
       model = User
       fields = ["username", "email", "password1", "password2"]