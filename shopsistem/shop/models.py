from django.db import models

# Create your models here.

class estabelecimento(models.Model):
    nome = models.CharField(max_length=65)
    logo = models.CharField(max_length=150)
    endereco = models.CharField(max_length=50)
    contato = models.CharField(max_length=50)
    status = models.CharField(max_length=10)

    class Meta:
        db_table = 'Estabelecimento'
    
    def __str__(self):
        return self.nome
    
    def __str__(self):
        return self.endereco

    def __str__(self):
        return self.status


class produto(models.Model):
    estabelecimento_id = models.ForeignKey(estabelecimento,on_delete=models.CASCADE)
    nome_prod = models.CharField(max_length=50,default=None)
    descricao = models.TextField(blank=True)
    fitness_food = models.BooleanField(default=False)
    brazilian_food = models.BooleanField(default=False)
    chinese_food = models.BooleanField(default=False)
    japanese_food = models.BooleanField(default=False)
    drink = models.BooleanField(default=False)
    fast_food = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    cake_or_pie = models.BooleanField(default=False)
    salad = models.BooleanField(default=False)
    price = models.CharField(max_length=5,default=None)

    class Meta:
        db_table = 'produto'

    
    def __str__(self):
        return self.nome_prod
    
    def __str__(self):
        return self.descricao
    
    def __str__(self):
        return self.price