# Generated by Django 2.0.2 on 2018-02-20 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atlasUpload', '0009_task_uploaddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='uploaddate',
            field=models.DateTimeField(default='2012-12-12 12:20', verbose_name='Date published'),
        ),
    ]
