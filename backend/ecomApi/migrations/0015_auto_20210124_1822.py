# Generated by Django 3.1.3 on 2021-01-24 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApi', '0014_auto_20210124_1819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-timestamp']},
        ),
    ]
