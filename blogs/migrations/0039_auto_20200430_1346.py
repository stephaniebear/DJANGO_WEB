# Generated by Django 3.0.4 on 2020-04-30 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0038_auto_20200430_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='office',
            old_name='status_flags',
            new_name='status_flag',
        ),
        migrations.RenameField(
            model_name='office',
            old_name='type',
            new_name='types',
        ),
    ]