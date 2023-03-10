# Generated by Django 4.1.4 on 2023-01-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='Código')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('foundation_local', models.CharField(max_length=100, verbose_name='Fundação')),
                ('foundation_date', models.DateField(verbose_name='Data da fundação')),
                ('founder', models.CharField(max_length=100, verbose_name='Fundador')),
                ('main', models.CharField(max_length=100, verbose_name='Sede')),
                ('billing', models.CharField(blank=True, max_length=100, null=True, verbose_name='Receita')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d', verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
    ]
