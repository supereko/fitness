from authapp.models import FitnessUser
from authapp.forms import FitnessUserEditForm


class FitnessUserAdminEditForm(FitnessUserEditForm):
    class Meta:
        model = FitnessUser
        fields = '__all__'
