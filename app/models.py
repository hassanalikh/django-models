from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    age = models.PositiveIntegerField()


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    salary = models.IntegerField
    status = models.CharField(max_length=15)
