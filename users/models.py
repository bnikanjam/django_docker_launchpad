from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    short_bio = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username or self.email
