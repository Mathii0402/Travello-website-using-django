# Generated by Django 4.0 on 2022-01-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_alter_destination_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
