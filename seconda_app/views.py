from django.shortcuts import render

# Create your views here.


def esif(request):
    context = {"var1": 5, "var2": 10}
    return render(request, "if.html", context)


def ifelse(request):
    context = {"var1": 10, "var2": 5}
    return render(request, "ifelse.html", context)


def ifelif(request):
    context = {"var1": 10, "var2": 5}
    return render(request, "ifelif.html", context)


def esfor(request):
    context = {"var1": 10}
    return render(request, "for.html", context)