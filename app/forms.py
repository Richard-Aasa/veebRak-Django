from django import forms
from .models import Calories

class CaloriesForm(forms.Form):
    food_item = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Toit',
        }),
        required=False)
    calories = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Kalorid (100g kohta)',
        }),
        required=False)

class DiaryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        choices = []
        for object in Calories.objects.all():
            choices.append((object.food_item, object.food_item))
        self.fields['food_item'].choices = choices

    food_item = forms.ChoiceField()
    amount = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Kogus (g)',
        }),
        required=False)