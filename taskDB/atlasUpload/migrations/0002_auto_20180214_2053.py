# Generated by Django 2.0.2 on 2018-02-14 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atlasUpload', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='name',
            new_name='aufgabenname',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='teacher',
            new_name='lehrer',
        ),
    ]