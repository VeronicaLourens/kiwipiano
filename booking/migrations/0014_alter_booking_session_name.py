# Generated by Django 3.2 on 2022-06-12 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_auto_20220612_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='session_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.session'),
        ),
    ]