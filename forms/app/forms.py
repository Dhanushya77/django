from django import forms
from .models import*

class User_form(forms.Form):
    Name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()
    
class Model_form(forms.ModelForm):
    
    class Meta:
        model = Sample
        fields = "__all__"
