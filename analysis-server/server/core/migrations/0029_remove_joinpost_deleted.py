# Generated by Django 3.2.5 on 2021-09-27 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_joinpost_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinpost',
            name='deleted',
        ),
    ]
