# Generated by Django 3.2.5 on 2021-09-27 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20210927_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtaghashtags',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reward',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
