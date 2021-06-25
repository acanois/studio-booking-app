from django import forms

class InputUserForm(forms.Form):
    first_name = forms.CharField(help_text='First Name', required=True)
    last_name = forms.CharField(help_text='Last Name', required=True)
    band_name = forms.CharField(help_text='Band Name', required=True)
    