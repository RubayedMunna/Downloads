from django.db import models
from day4app.models import Course

class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=40)
    courses = models.ManyToManyField(Course, related_name='students', blank=True)

    def __str__(self):
        return f"{self.roll}: {self.name}"
