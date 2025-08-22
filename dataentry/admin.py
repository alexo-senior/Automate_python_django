from django.contrib import admin
#para registrar el modelo y acceder al admin se debe importar la clase

from .models import Student

admin.site.register(Student)



