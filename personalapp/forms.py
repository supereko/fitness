from django import forms
from mainapp.models import Antropometry, Message
from django.forms.widgets import HiddenInput


class AddAntropometryForm(forms.ModelForm):
    class Meta:
        model = Antropometry
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddAntropometryForm, self).__init__(*args, **kwargs)
        self.fields['fitnessuser'].widget = HiddenInput()


class AddMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddMessageForm, self).__init__(*args, **kwargs)
        self.fields['fitnessuser'].widget = HiddenInput()