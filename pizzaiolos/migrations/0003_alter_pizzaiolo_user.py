# Generated by Django 3.2.7 on 2021-10-11 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pizzaiolos', '0002_auto_20211008_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzaiolo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]