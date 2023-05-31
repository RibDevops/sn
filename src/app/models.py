from django.db import models
from django.contrib.auth.models import User

class Tipo(models.Model):
    # id = models.AutoField(primary_key=True)
    tipo_doc = models.CharField(max_length=30)
    description_tipo = models.TextField()
    # image = models.ImageField(upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): # adicionar isso
        return self.tipo_doc
    
    class Meta:  # adicionar isso
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']

# Create your models here.
class Numeracao(models.Model):
    # id = models.AutoField(primary_key=True)
    fk_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(User, on_delete=models.PROTECT)
    # id_tipo = models.IntegerField()
    numero_doc = models.IntegerField()
    description_doc = models.TextField()
    # image = models.ImageField(upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): # adicionar isso
        return self.numero_doc, self.fk_tipo, self.fk_user, self.description_doc
    
    class Meta:  # adicionar isso
        verbose_name = 'Numero'
        verbose_name_plural = 'Numeros'
        ordering = ['id']
    





# Create your models here.
# class Carros(models.Model):
#     modelo = models.CharField(max_length=150)
#     marca = models.CharField(max_length=100)
#     ano = models.IntegerField()