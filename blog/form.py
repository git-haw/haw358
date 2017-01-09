import django.forms.forms
from django import forms

def LoginForm(request):
    if request is not None:
        return django.forms.forms(request)
    return django.forms.forms

class WriteForm(forms.Form):
    title = forms.CharField(max_length=32)
    content = forms.Textarea()