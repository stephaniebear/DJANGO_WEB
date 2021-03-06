# Generated by Django 3.0.4 on 2020-04-16 07:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0021_delete_resultdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultDetails',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('specifications', models.CharField(max_length=100)),
                ('result_flag', models.CharField(max_length=1)),
                ('result_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Result')),
            ],
        ),
    ]
