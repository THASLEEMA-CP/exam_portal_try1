from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    branch = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username



