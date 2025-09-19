from email.policy import default

from django.db import models
from stdimage import StdImageField

# Create your models here.

class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)


class Meta:
    abstract = True

class Cargo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200,
                                 blank=True, null=True)

    def __str__(self):
        return self.nome

class Funcionario(Base):
    nome = models.CharField(max_length=100)
    bio = models.TextField()
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL,
                              blank=True, null=True)
    foto = StdImageField(
        upload_to='equipe',
        variations=
         {
             'thumb':
             {
                 'width': 60,
                 'height': 60,
                 'crop':True
            }
         }
    )

class Meta:
    verbose_name = 'Funcionario'
    verbose_name_plural = 'Funcionarios'

def __str__(self):
    return self.nome