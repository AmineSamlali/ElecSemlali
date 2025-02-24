# Generated by Django 3.1.2 on 2020-11-18 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CTG_Name', models.CharField(max_length=90)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(blank=True, choices=[('NOUVEAU', 'NOUVEAU'), ('SOLDE', 'SOLDE'), ('BONNE_AFAIRE', 'BONNE AFAIRE'), ('EXCLUSIVE', 'EXCLUSIVE')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRD_Name', models.CharField(max_length=100)),
                ('PRD_discription', models.TextField(max_length=800)),
                ('PRD_Price', models.FloatField()),
                ('PRD_Null_price', models.FloatField(blank=True, null=True)),
                ('PRD_quantity', models.IntegerField()),
                ('PRD_image', models.ImageField(upload_to='products/')),
                ('PRD_added_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('PRD_Ctegory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.category')),
                ('PRD_type', models.ManyToManyField(to='Home.Tags')),
            ],
            options={
                'ordering': ['-PRD_added_at'],
            },
        ),
    ]
