# Generated by Django 4.1.4 on 2023-01-20 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='registration_date',
            field=models.DateField(verbose_name='Data de cadastro'),
        ),
    ]