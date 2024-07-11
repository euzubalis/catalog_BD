from .models import ConditionerOrder
from django import forms

class ConditionerOrderForm(forms.ModelForm):
    class Meta:
        model = ConditionerOrder
        fields = ['content']