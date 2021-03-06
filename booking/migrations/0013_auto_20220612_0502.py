# Generated by Django 3.2 on 2022-06-12 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_auto_20220611_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Exams-training', 'Exams-training'), ('Live-recital', 'Live-recital'), ('Virtual-performance', 'Virtual-performance'), ('Repertoire-recording', 'Repertoire-recording'), ('Online-recital', 'Online-recital'), ('End-of-year-concert', 'End-of-year-concert')], max_length=30)),
                ('session_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('session_status', models.IntegerField(choices=[(0, 'Available'), (1, 'Unavailable')], default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='lesson_name',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.AddField(
            model_name='booking',
            name='session_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='booking.session'),
        ),
    ]
