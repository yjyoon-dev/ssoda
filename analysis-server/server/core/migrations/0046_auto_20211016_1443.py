# Generated by Django 3.2.5 on 2021-10-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_alter_eventreport_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventreport',
            name='deleted',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='eventreport',
            name='event_status',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
