# Generated by Django 4.0.3 on 2022-03-29 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsellingApp', '0020_alter_availability_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='hours',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]