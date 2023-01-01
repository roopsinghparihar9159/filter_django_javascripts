from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=70)
    country_code = models.IntegerField()

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=70) 
    pincode = models.IntegerField()
    country = models.ForeignKey(Country,on_delete=models.CASCADE,blank=True,default=1)

    def __str__(self):
        return self.name