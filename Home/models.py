from django.db import models
from django.utils.functional import lazy as _
from django.utils.text import slugify
from random import *
from io import BytesIO
from PIL import Image
from django.core.files import File

def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO() 
    # save image to BytesIO object
    
    im.save(im_io, 'PNG', quality=50) 
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image

class Product(models.Model):
    PRD_Name = models.CharField(max_length=100)
    PRD_discription = models.TextField(max_length=800)
    PRD_Price = models.FloatField()
    PRD_Null_price = models.FloatField(blank=True,null=True)
    PRD_quantity = models.IntegerField()
    PRD_Ctegory = models.ForeignKey('Category',on_delete=models.CASCADE,blank=True , null=True)
    PRD_image = models.ImageField(upload_to='products/')
    PRD_added_at = models.DateTimeField(auto_now=True)
    PRD_type = models.ManyToManyField('Tags') 
    slug = models.SlugField(blank=True ,null=True)        
    class Meta:
        ordering =  [ '-PRD_added_at' ]
    def __str__(self):
        return self.PRD_Name
    
    def save(self,*args, **kwargs):
        i = randint(1,9)
        self.slug = slugify(self.PRD_Name)+'-'+str(i)

        new_image = compress(self.PRD_image)
        # set self.image to new_image
        self.PRD_image = new_image
        super(Product,self).save(*args, **kwargs)



    def __str__(self):
        return self.PRD_Name
class Category(models.Model):
    CTG_Name = models.CharField( max_length=90)
    slug = models.SlugField(blank=True , null=True)
    def save(self,*args, **kwargs):
        self.slug = slugify(self.CTG_Name)
        super(Category,self).save(*args, **kwargs)
    def __str__(self):
        return self.CTG_Name



class Tags(models.Model):
    choices = [
    ('NOUVEAU', 'NOUVEAU'),
    ('SOLDE', 'SOLDE'),
    ('BONNE_AFAIRE', 'BONNE AFAIRE'),
    ('EXCLUSIVE', 'EXCLUSIVE'),
]
    Type = models.CharField(max_length=50,choices=choices ,blank=True,null=True)

    def __str__(self):
        return self.Type
    


