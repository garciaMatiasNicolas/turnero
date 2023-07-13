from django.db import models
from django.contrib.auth.models import User

# Shift model
class Shifts(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    count_number = models.IntegerField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)