# Generated by Django 3.2.9 on 2022-03-15 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counsellingApp', '0011_alter_notifications_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notifications',
            options={'ordering': ['date'], 'verbose_name_plural': 'Notifications'},
        ),
    ]