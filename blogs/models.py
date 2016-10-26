from django.db import models

# Create your models here.
class BlogPost(models.Model):
    #Compos da tabela BlogPost
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    dataAdd = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto[:50] + '...'