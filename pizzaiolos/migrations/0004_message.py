# Generated by Django 3.2.7 on 2021-10-12 16:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaiolos', '0003_alter_pizzaiolo_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='pizzaiolos.pizzaiolo')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pizzaiolos.pizzaiolo')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]