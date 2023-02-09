from django.db import models

# Create your models here.

class Pokedex(models.Model): 
    region_id       = IntegerField() 
    identifier      = CharField(max_length=100)
    is_main_series  = IntegerField() 