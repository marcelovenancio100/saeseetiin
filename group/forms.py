from django.forms import ModelForm

from .models import Group


class FormGroup(ModelForm):
    class Meta:
        model = Group
        fields = ('code', 'name', 'description')
