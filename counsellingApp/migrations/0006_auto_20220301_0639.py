# Generated by Django 3.2.9 on 2022-03-01 06:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('counsellingApp', '0005_auto_20220301_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counsellor',
            name='user_id',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='supercounsellor',
            name='user_id',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=255, null=True),
        ),
    ]
