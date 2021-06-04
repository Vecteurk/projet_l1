from django.db import models


class Faculte(models.Model):
    nom = models.CharField(max_length=100)

class Filiere(models.Model):
    nom = models.CharField(max_length=100)
    faculte = models.ForeignKey(Faculte, on_delete=models.CASCADE)

class Etudiant(models.Model):
    nom = models.CharField(max_length=50)
    postnom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=50)
    sexe = models.CharField(max_length=2)
    adresse = models.CharField(max_length=150)
    mail = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    admission = models.BooleanField(default=False)


class Dossier(models.Model):
    etudiant = models.OneToOneField(Etudiant, on_delete=models.CASCADE)
    bultin_6 = models.FileField()
    journal = models.FileField()
    photo = models.FileField()
    



