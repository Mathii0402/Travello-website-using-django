# Generated by Django 4.0 on 2022-01-15 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='desc',
            field=models.TextField(max_length=100),
        ),
    ]
