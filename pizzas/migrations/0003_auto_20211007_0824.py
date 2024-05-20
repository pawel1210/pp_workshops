# Generated by Django 3.2.7 on 2021-10-07 08:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaiolos', '0001_initial'),
        ('pizzas', '0002_auto_20210917_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pizzaiolos.pizzaiolo')),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pizzaiolos.pizzaiolo'),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AddField(
            model_name='comment',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.pizza'),
        ),
    ]
