# Generated by Django 3.0.4 on 2020-05-01 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0010_auto_20200427_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='created_at',
            field=models.DateTimeField(blank=True, default='2020-04-27 21:26:18.341835'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='updated_at',
            field=models.DateTimeField(blank=True, default='2020-04-27 21:26:18.341835'),
        ),
    ]