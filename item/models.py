from django.db import models
from django.utils import timezone

from collection.models import Collection
from brand.models import Brand
from model.models import Model
from group.models import Group
from situation.models import Situation
from utils.image_utils import resize_image


class Item(models.Model):
    collection = models.ForeignKey(Collection, verbose_name='Coleção', on_delete=models.CASCADE)
    code = models.CharField(verbose_name='Código', max_length=10)
    name = models.CharField(verbose_name='Nome', max_length=100)
    description = models.CharField(verbose_name='Descrição', max_length=255)
    brand = models.ForeignKey(Brand, verbose_name='Marca', on_delete=models.CASCADE)
    model = models.ForeignKey(Model, verbose_name='Modelo', on_delete=models.CASCADE)
    identifier_code = models.CharField(verbose_name='Código de identificação', max_length=100, blank=True, null=True)
    serial_number = models.CharField(verbose_name='Número de série', max_length=100, blank=True, null=True)
    developer = models.CharField(verbose_name='Desenvolvedor', max_length=100, blank=True, null=True)
    distributor = models.CharField(verbose_name='Distribuidor', max_length=100, blank=True, null=True)
    release_year = models.PositiveIntegerField(verbose_name='Ano de lançamento', blank=True, null=True)
    manufacture_year = models.PositiveIntegerField(verbose_name='Ano de fabricação', blank=True, null=True)
    group = models.ForeignKey(Group, verbose_name='Grupo', on_delete=models.CASCADE)
    situation = models.ForeignKey(Situation, verbose_name='Situação', on_delete=models.CASCADE)
    market_value = models.DecimalField(verbose_name='Valor de mercado', max_digits=10, decimal_places=2)
    sale_value = models.DecimalField(verbose_name='Valor de venda', max_digits=10, decimal_places=2)
    original = models.BooleanField(verbose_name='É original', default=True)
    box = models.BooleanField(verbose_name='Tem caixa', default=True)
    original_box = models.BooleanField(verbose_name='Caixa original', default=True)
    negotiable = models.BooleanField(verbose_name='É negociável', default=True)
    registration_date = models.DateTimeField(verbose_name='Data de cadastro', editable=False)
    last_update_date = models.DateTimeField(verbose_name='Data da última atualização', editable=False)
    specifications = models.TextField(verbose_name='Especificações', blank=True, null=True)
    composition = models.TextField(verbose_name='Composição', blank=True, null=True)
    damages = models.TextField(verbose_name='Avarias', blank=True, null=True)
    comments = models.TextField(verbose_name='Observações', blank=True, null=True)
    photo1 = models.ImageField(verbose_name='Foto 1', upload_to='img/%Y/%m/%d', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='Foto 2', upload_to='img/%Y/%m/%d', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='Foto 3', upload_to='img/%Y/%m/%d', blank=True, null=True)
    photo4 = models.ImageField(verbose_name='Foto 4', upload_to='img/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.registration_date = timezone.now()

        self.last_update_date = timezone.now()

        super().save(*args, **kwargs)

        if self.photo1:
            resize_image(self.photo1.name, 800)

        if self.photo2:
            resize_image(self.photo2.name, 800)

        if self.photo3:
            resize_image(self.photo3.name, 800)

        if self.photo4:
            resize_image(self.photo4.name, 800)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
