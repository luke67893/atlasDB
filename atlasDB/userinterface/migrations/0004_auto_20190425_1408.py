# Generated by Django 2.2 on 2019-04-25 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinterface', '0003_auto_20190425_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
