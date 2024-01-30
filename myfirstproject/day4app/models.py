from django.db import models

class CourseTypeChoices(models.TextChoices):
    THEORY = 'THEORY', 'Theory Course'
    LAB = 'LAB', 'Lab Course'
    PROJECT = 'PROJECT', 'Project Course'

# Create your models here.
class Course(models.Model):
    course_id =models.CharField(max_length=10)
    course_name =models.CharField(max_length=40)
    course_credit=models.DecimalField(max_digits=4,decimal_places=2)
    course_type = models.CharField(max_length=10, choices=CourseTypeChoices.choices, default=CourseTypeChoices.THEORY)
    tutorial_full_marks=models.DecimalField(max_digits=4,decimal_places=2)
    final_full_marks=models.DecimalField(max_digits=4,decimal_places=2)
    att_full_marks=models.DecimalField(max_digits=4,decimal_places=2)
    
    def __str__(self):
        return self.course_id + ": "+self.course_name