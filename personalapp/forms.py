from django import forms
from mainapp.models import Antropometry


class AddAntropometryForm(forms.ModelForm):
    class Meta:
        model = Antropometry
        fields = '__all__'

