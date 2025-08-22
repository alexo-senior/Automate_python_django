from django.db import models

class Student(models.Model):
    roll_no = models.CharField('rol', max_length=10)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    #para ver la tabla creada luego de las migraciones 
    #se debe registrar en el admin de la app y luego ingresar
    
    
    
    
    
