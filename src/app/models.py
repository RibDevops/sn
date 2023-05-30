from django.db import models

class Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_doc = models.IntegerField()
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
    id = models.AutoField(primary_key=True)
    id_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    # id_tipo = models.IntegerField()
    numero_doc = models.IntegerField()
    description_doc = models.TextField()
    # image = models.ImageField(upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): # adicionar isso
        return self.numero_doc
    
    class Meta:  # adicionar isso
        verbose_name = 'Numero'
        verbose_name_plural = 'Numeros'
        ordering = ['id']
    





# Create your models here.
# class Carros(models.Model):
#     modelo = models.CharField(max_length=150)
#     marca = models.CharField(max_length=100)
#     ano = models.IntegerField()