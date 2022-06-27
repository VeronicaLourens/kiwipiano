# Generated by Django 3.2 on 2022-06-27 08:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0030_alter_booking_timeslot'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name_profile',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name_profile',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
