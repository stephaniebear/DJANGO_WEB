# Generated by Django 3.0.4 on 2020-04-23 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0031_auto_20200423_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_set', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
