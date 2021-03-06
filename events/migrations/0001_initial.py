# Generated by Django 3.0.4 on 2020-04-27 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parents', '0002_baby'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('baby_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parents.Baby')),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventType')),
            ],
        ),
    ]
