# Generated by Django 5.1.1 on 2024-11-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financialcalendar',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='financialcalendar',
            table='financial_calendar',
        ),
    ]
