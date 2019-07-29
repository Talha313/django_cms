from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import Form, ModelForm

from .models import Contact, Subscribe


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
