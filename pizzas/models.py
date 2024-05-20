from django.db import models
from pizzaiolos.models import Pizzaiolo
import uuid
import datetime

# Create your models here.

class Pizza(models.Model):
    owner = models.ForeignKey(Pizzaiolo, null=True, blank=True, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    was_edited = models.BooleanField(default=False, null=True)
    edited = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='pizzas/default.jpg', upload_to="pizzas/")
    style = models.ManyToManyField('Style', blank=True)
    flour = models.ManyToManyField('Flour', blank=True)
    def __str__(self):
        return self.title

    @property
    def created_str(self):
        today = str(datetime.datetime.today()).split(" ")[0]
        created_string = str(self.created).split(" ")[0]
        if today == created_string:
            return "Today"
        else:
            return created_string

    @property
    def edited_str(self):
        today = str(datetime.datetime.today()).split(" ")[0]
        edited_string = str(self.edited).split(" ")[0]
        if today == edited_string:
            return "Today"
        else:
            return edited_string


class Comment(models.Model):
    owner = models.ForeignKey(Pizzaiolo, null=True, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    was_edited = models.BooleanField(default=False, null=True)
    def __str__(self):
        return self.body

    class Meta:
        ordering = ["-created"]

class Flour(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Style(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
