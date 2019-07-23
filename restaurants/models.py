from django.db import models

# Create your models here.
'''
Each model is a Python class that subclasses django.db.models.Model.
Each attribute of the model represents a database field.
With all of this, Django gives you an automatically-generated database-access API; see Making queries.

'''
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    opening_time = models.CharField(max_length=30) #DateTimeField
    closing_time = models.CharField(max_length=30) # DateTimeField
    created_on = models.DateTimeField(auto_now_add=True)
