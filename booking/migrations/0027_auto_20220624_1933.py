# Generated by Django 3.2 on 2022-06-24 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0026_alter_booking_timeslot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='timeslot',
            field=models.IntegerField(choices=[(0, '09:00 - 10:00'), (1, '10:00 - 11:00'), (2, '11:00 - 12:00'), (3, '12:00 - 13:00'), (4, '13:00 - 14:00'), (5, '14:00 - 15:00'), (6, '15:00 - 16:00'), (7, '16:00 - 17:00')], default=0),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set(),
        ),
    ]
