from django import forms
from .models import Student
from day4app.models import Course
from django.forms import ChoiceField

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields= '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields= '__all__'        