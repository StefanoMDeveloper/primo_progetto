from django.urls import path
from .views import homepage, menu, chisiamo, variabili, index

app_name = "prima_app"
urlpatterns = [
    path("welcome/", homepage, name="homepage"),
    path("menu/", menu, name="menu"),
    path("chi-siamo/", chisiamo, name="chi-siamo"),
    path("variabili/", variabili, name="variabili"),
    path("index", index, name="index")
]
