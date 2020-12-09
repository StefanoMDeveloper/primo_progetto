from django.urls import path
from .views import AutoreDetail_MS, LibroList_MS

app_name = 'libreria'

urlpatterns = [
    path('', LibroList_MS.as_view(), name='lista_libri'),
    path('autore/<int:pk>/', AutoreDetail_MS.as_view(), name='profilo_autore')
]
