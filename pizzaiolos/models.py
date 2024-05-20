from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.
class Pizzaiolo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    oven = models.CharField(max_length=200, blank=True, null=True)
    mixer = models.CharField(max_length=200, blank=True, null=True)
    profile_img = models.ImageField(null=True, blank=True, upload_to='pizzaiolos/', default='pizzaiolos/user-default.png')
    social_instagram = models.CharField(max_length=200, blank=True, null=True)
    social_facebook = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['last_name']

    @property
    def name(self):
        name_string = f"{self.first_name} {self.last_name}"
        return name_string

    @property
    def unread(self):
        count = int(self.messages.filter(is_read=False).count())
        return count

    @property
    def pizzas_amount(self):
        amount = int(self.pizza_set.all().count())
        return amount


class Message(models.Model):
    sender = models.ForeignKey(Pizzaiolo, on_delete=models.SET_NULL, null=True)
    recipient = models.ForeignKey(Pizzaiolo, on_delete=models.SET_NULL, null=True, related_name="messages")
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.body

    class Meta:
        ordering = ["-created"]