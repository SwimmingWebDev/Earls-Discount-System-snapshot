# Generated by Django 5.1.1 on 2024-11-11 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_admin', '0003_alter_cardholder_hire_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardholder',
            name='hire_date',
        ),
    ]
