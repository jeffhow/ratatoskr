# Generated by Django 3.2.12 on 2022-04-05 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20220405_1356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='uuid',
            new_name='id',
        ),
    ]
