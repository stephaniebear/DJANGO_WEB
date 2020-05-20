# Generated by Django 3.0.4 on 2020-04-16 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_auto_20200416_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultdetails',
            name='id',
        ),
        migrations.AlterField(
            model_name='resultdetails',
            name='result_uuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='blogs.Result'),
        ),
    ]
