# Generated by Django 4.1.4 on 2023-01-25 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('model', '0001_initial'),
        ('group', '0001_initial'),
        ('brand', '0001_initial'),
        ('situation', '0001_initial'),
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='Código')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.CharField(max_length=255, verbose_name='Descrição')),
                ('identifier_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Código de identificação')),
                ('serial_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Número de série')),
                ('developer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Desenvolvedor')),
                ('distributor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Distribuidor')),
                ('release_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Ano de lançamento')),
                ('manufacture_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Ano de fabricação')),
                ('market_value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor de mercado')),
                ('sale_value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor de venda')),
                ('original', models.BooleanField(default=True, verbose_name='É original')),
                ('box', models.BooleanField(default=True, verbose_name='Tem caixa')),
                ('original_box', models.BooleanField(default=True, verbose_name='Caixa original')),
                ('negotiable', models.BooleanField(default=True, verbose_name='É negociável')),
                ('registration_date', models.DateTimeField(editable=False, verbose_name='Data de cadastro')),
                ('last_update_date', models.DateTimeField(editable=False, verbose_name='Data da última atualização')),
                ('specifications', models.TextField(blank=True, null=True, verbose_name='Especificações')),
                ('composition', models.TextField(blank=True, null=True, verbose_name='Composição')),
                ('damages', models.TextField(blank=True, null=True, verbose_name='Avarias')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d', verbose_name='Foto 1')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d', verbose_name='Foto 2')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d', verbose_name='Foto 3')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d', verbose_name='Foto 4')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand', verbose_name='Marca')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.collection', verbose_name='Coleção')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.group', verbose_name='Grupo')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.model', verbose_name='Modelo')),
                ('situation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='situation.situation', verbose_name='Situação')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
            },
        ),
    ]
