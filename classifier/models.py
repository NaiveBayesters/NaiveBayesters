from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Classifier(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    data = models.TextField()
