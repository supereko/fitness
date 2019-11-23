from authapp.models import FitnessUser
from authapp.forms import FitnessUserEditForm
from django import forms
from django.contrib.admin import widgets

from mainapp.models import Training, Schedule


class FitnessUserAdminEditForm(FitnessUserEditForm):
    class Meta:
        model = FitnessUser
        fields = '__all__'


class TrainingCreateForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class TrainingEditForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class ScheduleCreateForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['date', 'time', 'is_visit', 'training', 'fitnessuser']
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }

class ScheduleEditForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['date', 'time', 'is_visit', 'training', 'fitnessuser']
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

