# Generated by Django 4.0.4 on 2022-05-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_profile_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]