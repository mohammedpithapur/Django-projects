from django.db import models

# Create your models here.
class Students(models.Model):
    profile=models.ImageField(blank=True, null=True, upload_to='images/')
    name = models.CharField(max_length=60)
    enr = models.IntegerField()
    task = models.TextField(default='None')
    status = models.BooleanField(default=False)
    color=models.CharField(max_length=20,default='white',)