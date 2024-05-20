from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Pizzaiolo
from django.core.mail import send_mail
from django.conf import settings

def createPizzaiolo(sender, instance, created, **kwargs):
    if created:
        user = instance
        pizzaiolo = Pizzaiolo.objects.create(
            user = user,
            username = user.username,
            first_name = user.first_name,
            last_name = user.last_name,
            email = user.email,
        )

        subject = "Welcome to PizzaProject"
        message = f"Hello {pizzaiolo.first_name}, Welcome to PizzaProject. We're really happy that you decided to join us!"

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [pizzaiolo.email],
            fail_silently=False,
        )

def deleteUser(sender, instance, **kwargs):
    try:
        pizzaiolo = instance
        user = pizzaiolo.user
        user.delete()
    except:
        pass

post_save.connect(createPizzaiolo, sender=User)
post_delete.connect(deleteUser, sender=Pizzaiolo)