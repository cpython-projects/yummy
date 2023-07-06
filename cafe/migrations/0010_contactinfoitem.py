# Generated by Django 4.2.2 on 2023-07-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0009_event_short_desc_alter_event_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=250)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]
