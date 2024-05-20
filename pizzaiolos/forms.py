from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Pizzaiolo, Message

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class PizzaioloForm(ModelForm):
    class Meta:
        model = Pizzaiolo
        fields = ["location", "bio", "oven", "mixer", "profile_img", "social_instagram", "social_facebook"]

    def __init__(self, *args, **kwargs):
        super(PizzaioloForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["body"]

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})