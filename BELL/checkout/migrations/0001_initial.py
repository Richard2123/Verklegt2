# Generated by Django 4.0.4 on 2022-05-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemid', models.IntegerField()),
                ('sellerid', models.IntegerField()),
                ('buyerid', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]