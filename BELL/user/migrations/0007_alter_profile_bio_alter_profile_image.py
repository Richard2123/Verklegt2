# Generated by Django 4.0.4 on 2022-05-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_profile_bio_alter_profile_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.CharField(blank=True, default='https://cdn.vectorstock.com/i/1000x1000/45/79/male-avatar-profile-picture-silhouette-light-vector-4684579.webp', max_length=9999),
        ),
    ]