from django.db import models

# Create your models here.
class Numeracao(models.Model):
    id_sigla = models.IntegerField()
    id_sigla = models.IntegerField()
    numero_doc = models.IntegerField()
    description = models.TextField()
    # image = models.ImageField(upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): # adicionar isso
        return self.numero_doc
    
    class Meta:  # adicionar isso
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']


# Create your models here.
# class Carros(models.Model):
#     modelo = models.CharField(max_length=150)
#     marca = models.CharField(max_length=100)
#     ano = models.IntegerField()