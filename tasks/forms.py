from django import forms
from django.forms import ModelForm

from .models import Task


class DateInput(forms.DateField):
    date = 'date'


class TimeInput(forms.TimeField):
    time = 'time'


# class DateTime(forms.Form):
#     date = forms.DateField(widget=DateInput)
#     time = forms.TimeField(widget=TimeInput)


class TaskForm(forms.ModelForm):  # наследует класс формы
    custom_date = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M'])

    class Meta:
        model = Task
        fields = ('title', 'custom_date', 'complete')
