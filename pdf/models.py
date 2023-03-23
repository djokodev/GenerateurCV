from django.db import models

class Profile(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    competence = models.CharField(max_length=1000)
    langue = models.CharField(max_length=500)
    interet = models.CharField(max_length=500)
    titre = models.CharField(max_length=200)
    experience = models.TextField()
    education = models.TextField()
    photo = models.ImageField(upload_to="photos", blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['-date_added']
