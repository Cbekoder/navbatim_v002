from django.contrib.auth.models import AbstractUser
from django.db import models


ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('user', 'User'),
)

class User(AbstractUser):
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    photo = models.ImageField(upload_to='users', null=True, blank=True)


    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
