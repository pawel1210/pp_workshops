from django import forms
from django.forms import ModelForm

from .models import Pizza, Comment

class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ["title", "description", "image", "style", "flour" ]

    def __init__(self, *args, **kwargs):
        super(PizzaForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Add your comment here'})