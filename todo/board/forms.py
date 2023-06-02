from django import forms
from .models import TodoList


class DateInput(forms.DateInput):
    input_type = 'date'


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('title', 'content', 'end_date', 'is_complete')
        widgets = {
            'end_date': DateInput()
        }
