# Generated by Django 3.2.6 on 2022-09-09 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
