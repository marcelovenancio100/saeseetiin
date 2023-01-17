from django.forms import ModelForm

from .models import Situation


class SituationForm(ModelForm):
    class Meta:
        model = Situation
        fields = '__all__'
