from django.db import models


class Collection(models.Model):
    code = models.CharField(verbose_name='Código', max_length=30)
    name = models.CharField(verbose_name='Nome', max_length=100)
    description = models.CharField(verbose_name='Descrição', max_length=255)
    owner = models.CharField(verbose_name='Dono', max_length=100)
    responsible = models.CharField(verbose_name='Responsável', max_length=100)
    comments = models.TextField(verbose_name='Observações', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Coleção'
        verbose_name_plural = 'Coleções'


class Address(models.Model):
    collection = models.ForeignKey(Collection, verbose_name='Coleção', on_delete=models.CASCADE)
    zipcode = models.CharField(verbose_name='Cep', max_length=8)
    address = models.CharField(verbose_name='Endereço', max_length=50)
    number = models.CharField(verbose_name='Número', max_length=5)
    complement = models.CharField(verbose_name='Complemento', max_length=30, blank=True, null=True)
    district = models.CharField(verbose_name='Bairro', max_length=30)
    city = models.CharField(verbose_name='Município', max_length=30)
    state = models.CharField(verbose_name='Estado', max_length=2, default='SP', choices=(
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
    ))
    country = models.CharField(verbose_name='País', max_length=30)

    def __str__(self):
        return f'{self.address}'

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'


class Contact(models.Model):
    collection = models.ForeignKey(Collection, verbose_name='Coleção', on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='E-mail', max_length=100, blank=True, null=True)
    phone = models.CharField(verbose_name='Telefone', max_length=25, blank=True, null=True)
    cell = models.CharField(verbose_name='Celular', max_length=25, blank=True, null=True)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
