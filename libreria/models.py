from django.db import models

# Create your models here.
class Genere_MS(models.Model):
    genere = models.CharField(max_length=20)

    def __str__(self):
        return self.genere
    
    class Meta:
        verbose_name = "Genere"
        verbose_name_plural = "Generi"

class Autore_MS(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + " " + self.cognome

    class Meta:
        verbose_name = "Autore"
        verbose_name_plural = "Autori"

class Libro_MS(models.Model):
    titolo = models.CharField(max_length= 100)
    ISBN = models.CharField(max_length= 20)
    genere = models.ManyToManyField(Genere_MS)
    autore = models.ForeignKey(Autore_MS, on_delete=models.CASCADE, related_name="libri")

    def __str__(self):
        return self.titolo + " " + self.ISBN
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libri"