from django.db import models
from django.contrib.auth.models import User


class Specialites(models.Model):
    name =  models.CharField(max_length=20)
    praticien = models.ForeignKey(User,on_delete=models.CASCADE)

class Prestations(models.Model):
    name =  models.CharField(max_length=200)
    specialite = models.ForeignKey(Specialites, on_delete=models.CASCADE)


class Reservations(models.Model):
   date_reservation = models.DateTimeField('créneau')
   prestation = models.ForeignKey(Prestations, on_delete=models.CASCADE)
   patient = models.ForeignKey(User,on_delete=models.CASCADE)


class Disponibilite(models.Model):
    plage_horaire = models.DateField('plage horaire')
    specialite = models.ForeignKey(Specialites,on_delete=models.CASCADE)