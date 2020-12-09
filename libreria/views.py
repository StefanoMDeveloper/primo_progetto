from django.shortcuts import render, get_object_or_404
from .models import Libro_MS, Autore_MS
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.



def autore_MSDetailView(request, pk):
    autore = get_object_or_404(Autore_MS, pk=pk)
    context = {"autore": autore}
    return render(request, "autore.html", context)

class AutoreDetail_MS(DetailView):
    model= Autore_MS
    template_name= "autore.html"

class LibroList_MS(ListView):
    model = Libro_MS
    template_name = "lista_libri.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["libri"] = Libro_MS.objects.all()
        return context