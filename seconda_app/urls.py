from django.urls import path
from .views import homepage, esif, esifelse, esifelif

urlpatterns = [
    path('welcome/', homepage, name='home'),
    path('es_if/', esif, name='esif'),
    path('ifelse/', esifelse, name='ifelse'),
    path('ifelif/', esifelif, name='ifelif'),

]