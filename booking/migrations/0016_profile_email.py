# Generated by Django 3.2 on 2022-06-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0015_auto_20220613_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]