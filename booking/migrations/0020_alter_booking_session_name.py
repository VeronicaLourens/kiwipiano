# Generated by Django 3.2 on 2022-06-24 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0019_alter_booking_session_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='session_name',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Exams Training', 'Exams Training'), ('Live Recital', 'Live Recital'), ('Virtual Performance', 'Virtual Performance'), ('Repertoire Recording', 'Repertoire Recording'), ('Online Recital', 'Online Recital'), ('End Of Year Concert', 'End Of Year Concert')], default='Beginner', max_length=30),
        ),
    ]
