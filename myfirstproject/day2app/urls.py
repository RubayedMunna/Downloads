# day2app/urls.py
from django.urls import path
from . import views
from .views import student_list, student_info, course_list, assign_course, remove_course, homepage,courses, search_student

urlpatterns = [
    path('', homepage, name='homepage'),
    path('courses', courses, name='courses'),
    path('student_list', student_list, name='student_list'),
    path('search_student', search_student, name='search_student'),
    path('add_student', views.add_student, name='add_student'),
    path('save_student', views.save_student, name='save_student'),
    path('edit_student/<int:id>', views.edit_student, name='edit_student'),
    path('remove_student/<int:id>', views.remove_student, name='remove_student'),
    path('registration/<int:student_id>/', views.register, name='register'),
    path('student_info/<int:student_id>/', student_info, name='student_info'),
    path('course_list/', course_list, name='course_list'),
    path('assign_course/<int:student_id>/', assign_course, name='assign_course'),
    path('remove_course/<int:student_id>/<int:course_id>/', remove_course, name='remove_course'),
]
