# Generated by Django 3.2.6 on 2022-12-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_mailing_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='delivery_status',
            field=models.CharField(default='Scheduled', max_length=100),
        ),
    ]