# Generated by Django 3.1.2 on 2020-10-18 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20201018_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elec_semlali_info',
            name='Description',
            field=models.TextField(max_length=500),
        ),
    ]
