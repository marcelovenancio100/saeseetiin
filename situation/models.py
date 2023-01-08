from django.db import models


class Situation(models.Model):
    code = models.CharField(verbose_name='Código', max_length=10)
    name = models.CharField(verbose_name='Nome', max_length=100)
    description = models.CharField(verbose_name='Descrição', max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Situação'
        verbose_name_plural = 'Situações'
