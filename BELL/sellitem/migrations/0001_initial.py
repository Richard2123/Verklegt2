# Generated by Django 4.0.4 on 2022-05-09 13:22

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('itemname', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('base_price', models.FloatField()),
                ('main_image', models.IntegerField()),
                ('other_images', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('userid', models.IntegerField()),
                ('user_rank', models.CharField(blank=True, max_length=255)),
                ('starting_price', models.FloatField()),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('first_image', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='sellitem.itemimage')),
            ],
        ),
    ]