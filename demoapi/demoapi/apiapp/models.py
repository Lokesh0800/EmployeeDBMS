
from django.db import models

# Create your models here.
class desc(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500,default='')

    def __str__(self):
        return self.title