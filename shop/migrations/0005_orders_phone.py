# Generated by Django 3.2.7 on 2021-10-04 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default=' ', max_length=111),
        ),
    ]
