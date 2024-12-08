# Generated by Django 5.1.1 on 2024-09-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True, default=''),
        ),
    ]
