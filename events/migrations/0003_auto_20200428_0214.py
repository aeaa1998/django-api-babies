# Generated by Django 3.0.4 on 2020-04-28 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200427_1425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'permissions': (('see_event', 'See event'),)},
        ),
    ]
