#creamos un comando personalizado

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Prints Hello World"
    
    #aqui va la logica de todo
    #siempre se self en una funcion como argumento dentro de una clase
    #*args para recibir argumentos cualquiera, y kwargs para reecibir
    #argumentos clave
    def handle(self, *args, **kwargs):
        self.stdout.write('Hello World')
    #se produce una salida estatica
    

