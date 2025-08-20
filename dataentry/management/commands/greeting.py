#creamos un comando personalizado

from django.core.management.base import BaseCommand

#proposed command = python manage.py greeting Jhon(dynamic)
#proposed output Hi{name}, Good Morning

class Command(BaseCommand):
    help = "Greets the User"
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies user name')
        
        
    #funcion principal
    def handle(self, *args, **kwargs):
        #se usa kwargs porque el nombre es una palabra clave y acepta cualquiera
        name = kwargs['name']
        greeting = f'Hi {name}, Good Morning!'
        #self.stdout.write(greeting)
    #si quiero mostrar como un mensaje de exito en la consola
    #sale en color verde y en formato negrita
        self.stdout.write(self.style.SUCCESS(greeting))