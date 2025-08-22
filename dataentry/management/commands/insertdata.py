#I want to add some data to the database using the custom command
from django.core.management.base import BaseCommand
#desde la app dataentry punto models importar student
from dataentry.models import Student



#la finalidad es añadir datos a la base ded datos
#para eso se debe configurar el modelo

class Command(BaseCommand):
    help = 'I wil insert data to the Database'
    
    def handle(self, *args, **kwargs):
        #logic here 
        #add one data
        #add many data
        dataset = [
            {'roll_no':1002, 'name': 'Daniel', 'age': 26},
            {'roll_no':1003, 'name': 'Diego', 'age': 24},
            {'roll_no':1004, 'name': 'Tatiana', 'age': 48}
        ]
        #para insertar se hace un ciclo for que recorre el diccionario dataset
        for data in dataset:
            #print(data['name'])
            #para que tome los datos se usa el nombre itinerante de data y el valor
            Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            
        self.stdout.write(self.style.SUCCESS('data inserted successfuly!'))
        #el print es para probar por terminal el exito del ciclo
        #se ejecuta la insercion y muestra el mensaje de exito
        #se comprueba en el admin
        
        
    