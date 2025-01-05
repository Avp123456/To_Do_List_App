# base/forms.py
from django import forms

class PositionForm(forms.Form):
    position = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 10, 'cols': 30}),
        required=True
    )
