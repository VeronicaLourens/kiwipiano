# Generated by Django 3.2 on 2022-06-24 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_remove_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='session_name',
            field=models.CharField(choices=[('BE', 'Beginner'), ('IN', 'Intermediate'), ('AD', 'Advanced'), ('ET', 'Exams-training'), ('LR', 'Live-recital'), ('VP', 'Virtual-performance'), ('RR', 'Repertoire-recording'), ('OR', 'Online-recital'), ('EC', 'End-of-year-concert')], default='BE', max_length=30),
        ),
    ]
