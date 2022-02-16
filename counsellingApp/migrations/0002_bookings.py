# Generated by Django 3.2.9 on 2022-02-15 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsellingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(blank=True, default=None, null=True)),
                ('student_name', models.CharField(blank=True, db_index=True, default=None, max_length=255, null=True)),
                ('student_profile', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('date', models.CharField(blank=True, choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday')], default=None, max_length=255, null=True)),
                ('start_time', models.TimeField(blank=True, default=None, null=True)),
                ('end_time', models.TimeField(blank=True, default=None, null=True)),
                ('student_status', models.CharField(blank=True, db_index=True, default='Pending', max_length=255, null=True)),
            ],
        ),
    ]
