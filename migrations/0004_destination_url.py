# Generated by Django 4.0 on 2022-01-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_destination_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='url',
            field=models.URLField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
