# Generated by Django 5.1.6 on 2025-02-21 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=100)),
                ('demand_factor', models.FloatField()),
                ('urgency', models.FloatField()),
                ('location_adjustment', models.FloatField()),
            ],
        ),
    ]
