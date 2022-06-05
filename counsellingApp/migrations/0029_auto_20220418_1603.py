# Generated by Django 3.2.9 on 2022-04-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counsellingApp', '0028_auto_20220418_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='hours',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='availability',
            name='slots',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=255, null=True),
        ),
    ]