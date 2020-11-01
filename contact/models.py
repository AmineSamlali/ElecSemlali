from django.db import models
from django.utils.functional import lazy





class Elec_semlali_info(models.Model):
    Web_site_Name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField( max_length=254)
    Adress = models.TextField(max_length=400)
    number = models.CharField(max_length=40)
    fix = models.CharField( max_length=40)
    Description = models.TextField( max_length=500)
    faceBook = models.URLField(max_length=450)
    twitter = models.URLField(max_length=450)
    google_plus = models.URLField(max_length=450)
    linkdin = models.URLField(max_length=450)

    def __str__(self):
        return self.Web_site_Name