from django import forms

class Taskforms(forms.Form):
    task_name = forms.CharField(label="Task name")
    task_date = forms.DateField(label="Date")