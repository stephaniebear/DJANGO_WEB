# Generated by Django 3.0.4 on 2020-03-31 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_post_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('type_office', models.CharField(max_length=100)),
                ('specifications', models.CharField(max_length=100)),
                ('book_number', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=1)),
                ('desc', models.TextField()),
            ],
        ),
    ]
