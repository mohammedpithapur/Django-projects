from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=60)
    enr = models.IntegerField()
    marks = models.FloatField()