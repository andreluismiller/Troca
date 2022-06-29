from django.db import models
from django.db import models
from datetime import datetime 
from django.urls import reverse
from django.forms import ModelForm

"""
Modelo para o produtor
Irá ser o responsável pelo cadastro de produtos e cestas
"""
class Produtor(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=11)
    email = models.EmailField()
    senha = models.CharField(max_length=20)

    # to save the data
    def register(self):
        self.save()
  
    @staticmethod
    def get_produtor_by_email(email):
        try:
            return Produtor.objects.get(email=email)
        except:
            return False
  
    def isExists(self):
        if Produtor.objects.filter(email=self.email):
            return True
  
        return False




"""
Model para cadastro de produtos
"""
class Alimento(models.Model):
        
    LISTA_CATEGORIA = (
        ('f', 'Fruta'),
        ('l', 'Legume'),
        ('v', 'Verdura'),
        ('t', 'Ervas e temperos'),
        ('p', 'Produto lácteo (leite, queijo, etc.)'),
        ('o', 'Outros')
    )    
    categoria = models.CharField(max_length=1, choices=LISTA_CATEGORIA, default='f', blank=True)
    
    TIPO_PRODUCAO = (
        ('t', 'Agricultura tradicional'),
        ('o', 'Agricultura orgânica')
    )
    cultura = models.CharField(max_length=1, choices=TIPO_PRODUCAO, default='t', blank=True, help_text='Tipo de cultura do produto')
    descricao = models.CharField(max_length=100, blank=True, help_text='Nome do alimento')
    
    def __str__(self):
        return self.descricao

    @staticmethod
    def get_alimentos_por_id(ids):
        return Alimento.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_alimentos():
        return Alimento.objects.all()
  
"""
Form para o cadastro de produtos
"""
class ProdutoForm(ModelForm):
    class Meta:
        model = Alimento
        fields = '__all__'



"""
Model para cadastro de cesta
Deverá conter 2 ou mais produtos
"""
class Cesta(models.Model):
    produtor = models.ForeignKey(Produtor, on_delete=models.CASCADE)
    resumo = models.CharField(max_length=500, null=True, help_text="Descrição resumida")
    produtos = models.ManyToManyField(Alimento, on_delete=models.CASCADE)
    valor_estimado = models.FloatField()
   
    STATUS_DISPONIBILIDADE = (
        ('d', 'Disponível'),
        ('r', 'Reservada'),
        ('n', 'Não disponível')
    )
    disponibilidade = models.CharField(max_length=1, choices=STATUS_DISPONIBILIDADE, default='d', blank=True)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)
    data_retirada = models.DateField(null=True, blank=True)
    imagem = models.ImageField(upload_to='uploads/imagens/')

    # @property
    # def ImagemURL(self):
    #     try:
    #         url = self.imagem.url
    #     except:
    #         url = ''
    #     return url

    def __str__(self):
        return self.resumo
    
    def cadastroCesta(self):
        self.save()

    @staticmethod
    def get_cestas_por_produtor(produtor_id):
        return Cesta.objects.filter(produtor=produtor_id).order_by('-data_cadastro')


class CestForm(ModelForm):
    class meta:
        model = Cesta
        fields = ['produtor', 'resumo', 'produtos', 'valor estimado' 'disponibilidade', 'data_retirada']



