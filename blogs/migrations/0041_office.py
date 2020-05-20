# Generated by Django 3.0.4 on 2020-04-30 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0040_delete_office'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('office_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('province', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('types', models.CharField(max_length=1)),
                ('size', models.CharField(max_length=100)),
                ('status_flag', models.CharField(max_length=1)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('update_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
