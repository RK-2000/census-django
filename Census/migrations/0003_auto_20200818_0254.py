# Generated by Django 3.0.8 on 2020-08-17 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Census', '0002_auto_20200818_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]