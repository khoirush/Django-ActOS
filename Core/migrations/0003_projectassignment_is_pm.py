# Generated by Django 2.2.2 on 2019-06-14 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_auto_20190614_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectassignment',
            name='is_PM',
            field=models.BooleanField(default=False),
        ),
    ]
