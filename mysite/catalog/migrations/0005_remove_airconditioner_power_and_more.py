# Generated by Django 5.0.6 on 2024-07-08 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_manufacturer_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airconditioner',
            name='power',
        ),
        migrations.RemoveField(
            model_name='airconditioner',
            name='price',
        ),
        migrations.AddField(
            model_name='technicalspecification',
            name='power',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Galingumas (kW)'),
        ),
        migrations.AddField(
            model_name='technicalspecification',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Kaina'),
        ),
        migrations.AlterField(
            model_name='airconditioner',
            name='description',
            field=models.TextField(default='', max_length=5000, verbose_name='Aprašymas'),
        ),
    ]
