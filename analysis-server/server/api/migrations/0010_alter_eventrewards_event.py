# Generated by Django 3.2.5 on 2021-07-31 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_rewards_id_joinpost_rewards_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventrewards',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_rewards', to='api.event'),
        ),
    ]
