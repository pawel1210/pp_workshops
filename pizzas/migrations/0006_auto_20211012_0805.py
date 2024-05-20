# Generated by Django 3.2.7 on 2021-10-12 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0005_auto_20211011_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='modified',
            new_name='edited',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='modified',
            new_name='edited',
        ),
        migrations.AddField(
            model_name='comment',
            name='was_edited',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='pizza',
            name='was_edited',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
