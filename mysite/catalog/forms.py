from .models import ConditionerOrder, Profile
from django import forms
from django.contrib.auth.models import User

class ConditionerOrderForm(forms.ModelForm):
    class Meta:
        model = ConditionerOrder
        fields = ['content']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']