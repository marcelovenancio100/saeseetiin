from django.db import models


class Address(models.Model):
    adr_zipcode = models.CharField(verbose_name='Cep', max_length=8)
    adr_address = models.CharField(verbose_name='Endereço', max_length=50)
    adr_number = models.CharField(verbose_name='Número', max_length=5)
    adr_complement = models.CharField(verbose_name='Complemento', max_length=30, blank=True, null=True)
    adr_district = models.CharField(verbose_name='Bairro', max_length=30)
    adr_city = models.CharField(verbose_name='Município', max_length=30)
    adr_state = models.CharField(verbose_name='UF', max_length=2, default='SP', choices=(
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )),
    adr_country = models.CharField(verbose_name='País', max_length=30)

    def __str__(self):
        return f'{self.adr_address}'

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
