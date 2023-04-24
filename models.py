from django.db import models
from super_types.models import SuperType






# Create your models here.
class Super(models.Model):
    name = models. CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catch_phrase = models.CharField(max_length=255)
    type_of_super = models.ForeignKey(SuperType, on_delete=models.CASCADE, null=True )
    

    
    
    
