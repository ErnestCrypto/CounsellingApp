# Generated by Django 3.2.9 on 2022-02-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsellingApp', '0008_meetings_counsellor_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]