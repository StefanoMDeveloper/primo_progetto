from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return render(request, "homepage.html")


def menu(request):
    return render(request, "menu.html")


def chisiamo(request):
    return render(request, "chi-siamo.html")


def variabili(request):
    context = {
        "var1": "Variabile numero 1",
        "var2": "Variabile numero 2",
        "var3": "Variabile numero 3",
    }
    return render(request, "variabili.html", context)


def index(request):
    return render(request, "index.html")
