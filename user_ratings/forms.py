from django import forms
from .models import UserRating


class RatingForm(forms.ModelForm):
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={
        'required': 'False',
    }), required=False)

    class Meta:
        model = UserRating
        fields = ['rating']
