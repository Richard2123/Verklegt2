# Generated by Django 4.0.4 on 2022-05-12 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='rating',
            field=models.FloatField(default=2.5),
        ),
    ]