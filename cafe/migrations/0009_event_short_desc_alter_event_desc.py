# Generated by Django 4.2.2 on 2023-07-04 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0008_alter_event_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='short_desc',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
