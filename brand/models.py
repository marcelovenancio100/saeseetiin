from django.db import models

from utils.image_utils import resize_image


class Brand(models.Model):
    code = models.CharField(verbose_name='Código', max_length=10)
    name = models.CharField(verbose_name='Nome', max_length=100)
    description = models.TextField(verbose_name='Descrição')
    foundation_local = models.CharField(verbose_name='Fundação', max_length=100)
    foundation_date = models.DateField(verbose_name='Data da fundação')
    founder = models.CharField(verbose_name='Fundador', max_length=100)
    main = models.CharField(verbose_name='Sede', max_length=100)
    billing = models.CharField(verbose_name='Receita', max_length=100, blank=True, null=True)
    logo = models.ImageField(verbose_name='Logo', upload_to='img/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.logo:
            resize_image(self.logo.name, 800)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
