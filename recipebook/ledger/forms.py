from django import forms


class Taskforms(forms.Form):
    name = forms.CharField(label="Username")
    password = forms.CharField(label="Password")
