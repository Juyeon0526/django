from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Phone(models.Model):
    name = models.CharField('NAME', max_length=50, blank=True)
    phonenum = models.CharField('PHONE NUMBER', max_length=20, unique=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('phone:detail', kwargs={'pk':self.id})
