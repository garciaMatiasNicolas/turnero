from django.forms import ModelForm
from .models import Shifts

class ShiftForm(ModelForm):
    class Meta:
        model = Shifts
        fields = ['date', 'name', 'email', 'count_number']