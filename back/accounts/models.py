from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    college_name = models.CharField(max_length=128)
    graduation_completion = models.DateField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=64)
    t_shirt_size = models.CharField(max_length=3, null=True, blank=True)

    linkedin_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username