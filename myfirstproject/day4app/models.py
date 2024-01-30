from django.db import models

# Create your models here.
class Course(models.Model):
    course_id =models.CharField(max_length=10)
    course_name =models.CharField(max_length=40)
    course_credit=models.DecimalField(max_digits=4,decimal_places=2)
    tutorial_full_marks=models.DecimalField(max_digits=4,decimal_places=2)
    final_full_marks=models.DecimalField(max_digits=4,decimal_places=2)
    att_full_marks=models.DecimalField(max_digits=4,decimal_places=2)
    
    def __str__(self):
        return self.course_id + ": "+self.course_name