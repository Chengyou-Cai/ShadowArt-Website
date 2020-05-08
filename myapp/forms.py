from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from django.contrib.auth.models import User
from .models import Comments


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': '请输入您的邮箱'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
        widgets = {
            'username': forms.TextInput(attrs = {'placeholder': '请输入用户名'}),

        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
                                                               'placeholder': '请输入密码'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={ 'placeholder': '请重复您的密码'})
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        # user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']


        if commit:
            user.save()
        return user

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']