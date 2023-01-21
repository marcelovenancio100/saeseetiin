from django.forms import ModelForm

from .models import Collection, Address, Contact


class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = '__all__'


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
