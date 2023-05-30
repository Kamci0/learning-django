from django.db import models

class Ziomki(models.Model):
    imie = models.CharField(max_length=30)
    klata = models.IntegerField()
    przysiad = models.IntegerField()

    def __str__(self):
        return f'Rekordy ziomka {self.imie}'