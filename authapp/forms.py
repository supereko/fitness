from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from django import forms
from authapp.models import FitnessUser


class FitnessUserLoginForm(AuthenticationForm):
    class Meta:
        model = FitnessUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(FitnessUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class FitnessUserRegisterForm(UserCreationForm):
    class Meta:
        model = FitnessUser
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'date_birth', 'avatar')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class FitnessUserEditForm(UserChangeForm):
    class Meta:
        model = FitnessUser
        fields = ('username', 'first_name', 'last_name', 'email', 'date_birth', 'avatar', 'password')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()
