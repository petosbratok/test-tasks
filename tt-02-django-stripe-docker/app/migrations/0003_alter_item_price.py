# Generated by Django 3.2.6 on 2022-09-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_type_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]