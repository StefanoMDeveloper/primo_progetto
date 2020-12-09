from django.contrib import admin

# Register your models here.
from .models import Genere_MS, Autore_MS, Libro_MS

admin.site.register(Genere_MS)
admin.site.register(Autore_MS)
admin.site.register(Libro_MS)