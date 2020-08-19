from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    address  = models.CharField(max_length=100)
    phone = models.CharField(max_length=16)

    class Meta:
        ordering = ['id']