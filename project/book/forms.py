from django import forms
from . import models


class CreatePersonForm(forms.ModelForm):
    phones = forms.CharField(widget=forms.Textarea, help_text="Если у пользователя более одного номера, то каждый последующий вводить с новой строки при помощи 'Enter'")

    class Meta:
        model = models.Person
        fields = (
            'name',
            'phones'
        )
