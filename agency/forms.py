from django import forms
from django.contrib.auth.forms import UserCreationForm

from agency.models import Redactor


class RedactorCreateForm(UserCreationForm):
    class Meta:
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
        )


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": " Search by name...",
            "class": "rounded form-control bg-transparent"
        })
    )


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": " Search by title...",
            "class": "rounded form-control bg-transparent"
        })
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": " Search by username...",
            "class": "rounded form-control bg-transparent"
        })
    )
