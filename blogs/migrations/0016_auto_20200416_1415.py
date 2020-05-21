# Generated by Django 3.0.4 on 2020-04-16 07:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_auto_20200416_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultdetails',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='resultdetails',
            name='result_uuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Result'),
        ),
    ]