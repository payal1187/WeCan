from django.forms import ModelForm
from .models import ContactModel
from django import forms





class ContactForm(forms.ModelForm):
    email = forms.EmailField()
    concern = forms.TextInput()
    class Meta:
        model = ContactModel
        fields  = ['email','concern']
		
		
	

