from .models import Note, Brand, Fragrance
from django import forms
from django.contrib import admin
from .models import Fragrance


class FragranceAdminForm(forms.ModelForm):
    rating_admin = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'type': 'number',
            'min': '0',
            'max': '5',
            'step': '1',
        })
    )

    class Meta:
        model = Fragrance
        fields = '__all__'


