# Generated by Django 3.2.9 on 2022-02-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsellingApp', '0007_alter_bookings_student_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetings',
            name='counsellor_user_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
