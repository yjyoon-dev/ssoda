# Generated by Django 3.2.5 on 2021-09-30 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_event_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRefreshToken',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('refresh_token', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'user_refresh_token',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='eventimages',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='hashtag',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='hashtaghashtags',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='hashtagrequirements',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='reward',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='store',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='storeimages',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'managed': False},
        ),
    ]
