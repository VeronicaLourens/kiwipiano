# Generated by Django 3.2 on 2022-07-04 09:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0035_auto_20220630_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='message',
            field=models.TextField(blank=True, default='', max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alpha[ A - Z] characters are allowed.')]),
        ),
    ]
