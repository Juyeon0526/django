from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField('NAME', max_length=100, blank=False)
    studentnum = models.CharField('STUDENTNUM', max_length=50, blank=False)
    tel = models.CharField('MOBILE', max_length=50, blank=False)
    email = models.EmailField('EMAIL', max_length=50,blank=True)
    lecture = models.CharField('LECTURE', max_length=100, blank=False)
    professor = models.CharField('PROFESSOR', max_length=100, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('lecture','name',)

    def get_absolute_url(self):
        return reverse('student:student_detail', kwargs={'pk':self.id})