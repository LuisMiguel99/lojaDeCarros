from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name



class Car(models.Model):
    id = models.AutoField(primary_key=True) #indentificação do carro
    model = models.CharField(max_length=200) #modelo do carro
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True,null=True) #ano de fabricação
    model_year = models.IntegerField(blank=True,null=True) #ano do modelo
    plate = models.CharField(max_length=200,blank=True,null=True)
    value = models.FloatField(blank=True,null=True) #valor do carro

    def __str__(self):
        return self.model #função para substituir nome padrao do django no site 
    
    


