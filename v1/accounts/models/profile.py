from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username
