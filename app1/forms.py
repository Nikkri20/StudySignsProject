from django import forms
from .models import *


class SignForm(forms.ModelForm):
    class Meta:
        model = Sign
        fields = ['name', 'description', 'category', 'photo', 'realObjectPhoto']


class TestForm(forms.ModelForm):
    class Meta:
        model = Sign
        fields = ['question', 'answer', 'photo', 'realObjectPhoto']


class ExamForm(forms.ModelForm):
    class Meta:
        model = Sign
        fields = ['question', 'photo', 'realObjectPhoto']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Sign
        fields = ['name', 'description', 'category']
