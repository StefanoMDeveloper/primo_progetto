from django.urls import path
from .views import esif, ifelse, ifelif, esfor

app_name = "seconda_app"
urlpatterns = [
    path("if/", esif, name="if"),
    path("ifelse/", ifelse, name="ifelse"),
    path("ifelif/", ifelif, name="ifelif"),
    path("for/", esfor, name="for"),
]
