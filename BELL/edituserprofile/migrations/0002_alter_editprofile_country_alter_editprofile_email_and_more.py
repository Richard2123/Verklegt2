# Generated by Django 4.0.4 on 2022-05-11 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edituserprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editprofile',
            name='country',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='editprofile',
            name='email',
            field=models.EmailField(default='unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='editprofile',
            name='full_name',
            field=models.CharField(default='unknown', max_length=255),
        ),
    ]