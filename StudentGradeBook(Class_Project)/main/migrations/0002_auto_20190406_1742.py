# Generated by Django 2.0.7 on 2019-04-06 17:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Age must be postive')]),
        ),
    ]