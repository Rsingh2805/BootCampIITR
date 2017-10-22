from django.contrib.auth.models import User
from django import forms
from .models import Project


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ['username', 'password']


class AddProjectForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    github_link = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Project
        fields = ['title', 'description', 'github_link']
