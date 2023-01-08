from django.db import models
from django.conf import settings
from PIL import Image
import os

from collection.models import Collection
from group.models import Group
from situation.models import Situation


class Item(models.Model):
    collection = models.ForeignKey(Collection, verbose_name='Coleção', on_delete=models.CASCADE)
    code = models.CharField(verbose_name='Código', max_length=10)
    name = models.CharField(verbose_name='Nome', max_length=100)
    brand = models.CharField(verbose_name='Marca', max_length=100)
    model = models.CharField(verbose_name='Modelo', max_length=100)
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
    registration_date = models.DateField(verbose_name='Data de cadastro', auto_now=True)
    specifications = models.TextField(verbose_name='Especificações', blank=True, null=True)
    damages = models.TextField(verbose_name='Avarias', blank=True, null=True)
    comments = models.TextField(verbose_name='Observações', blank=True, null=True)
    photo1 = models.ImageField(verbose_name='Foto 1', upload_to='img/%Y/%m/%d', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='Foto 2', upload_to='img/%Y/%m/%d', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='Foto 3', upload_to='img/%Y/%m/%d', blank=True, null=True)
    photo4 = models.ImageField(verbose_name='Foto 4', upload_to='img/%Y/%m/%d', blank=True, null=True)
    photo5 = models.ImageField(verbose_name='Foto 5', upload_to='img/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo1:
            self.resize_image(self.photo1.name, 800)

        if self.photo2:
            self.resize_image(self.photo2.name, 800)

        if self.photo3:
            self.resize_image(self.photo3.name, 800)

        if self.photo4:
            self.resize_image(self.photo4.name, 800)

        if self.photo5:
            self.resize_image(self.photo5.name, 800)

    @staticmethod
    def resize_image(image_name, new_width):
        image_path = os.path.join(settings.MEDIA_ROOT, image_name)
        image = Image.open(image_path)
        width, height = image.size
        new_height = round((new_width * height) / width)

        if width <= new_width:
            image.close()
            return

        new_image = image.resize((new_width, new_height), Image.ANTIALIAS)
        new_image.save(image_path, optimize=True, quality=60)
        new_image.close()

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
