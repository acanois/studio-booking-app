# Generated by Django 3.2.5 on 2021-07-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_auto_20210709_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studiobooking',
            name='end_date',
            field=models.DateTimeField(default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='studiobooking',
            name='start_date',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
