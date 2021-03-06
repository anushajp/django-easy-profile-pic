from django import forms
from easy_profile_pic.fields import ProfilePicField



class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=70)
    phone = forms.RegexField(regex=r'^[\+]?(\d\-?){8,12}\d$', max_length=20)
    Picture = ProfilePicField()
