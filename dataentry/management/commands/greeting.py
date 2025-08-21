#creamos un comando personalizado

from django.core.management.base import BaseCommand

#proposed command = python manage.py greeting Jhon(dynamic)
#proposed output Hi{name}, Good Morning

class Command(BaseCommand):
    help = "Greets to the Users Everyday"
    
    def add_arguments(self, parser):
        parser.add_argument('name',  type=str, help='Specifies user name')
        parser.add_argument('lastname',  type=str, help='Specifies user lastname')
        
        
    #funcion principal
    def handle(self, *args, **kwargs):
        #se usa kwargs porque el nombre es una palabra clave y acepta cualquiera
        #se puede añadir el apellido con igual logica
        name = kwargs['name']
        lastname = kwargs['lastname']
        greeting = f'Hi {name} {lastname}, Good Morning!'
        #self.stdout.write(greeting)
    #si quiero mostrar como un mensaje de exito en la consola
    #sale en color verde y en formato negrita
        self.stdout.write(self.style.SUCCESS(greeting))
        