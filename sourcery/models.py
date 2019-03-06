from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Resource_Type(models.Model):
    name = models.CharField(max_length=50)
    deletedOn = models.DateField(default=None, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Resource(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    note = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=500)
    deletedOn = models.DateField(default=None, null=True)
    isCompleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_type = models.ForeignKey(Resource_Type, on_delete=models.CASCADE)

