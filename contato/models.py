from django.db import models

# Create your models here.
class Contato(models.Model):
    assunto = models.CharField(max_length=50)
    email = models.EmailField()
    descricao = models.TextField()

    def __str__(self):
        return self.assunto
