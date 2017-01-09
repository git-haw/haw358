import django.forms.forms

def LoginForm(request):
    if request is not None:
        return django.forms.forms(request)
    return django.forms.forms
