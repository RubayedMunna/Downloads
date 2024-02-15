
from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Student, Course
from django.http import HttpResponse
from .forms import StudentForm, CourseForm


def student_list(request):
    all_students = Student.objects.all()
    return render(request, 'day2/index.html', {'all_students': all_students})

def student_info(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'day2/show_student_info/student_info.html', {'student': student})

def course_list(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    unassigned_courses = Course.objects.exclude(student__id=student_id)
    return render(request, 'day2/show_student_info/course_list.html', {'student': student, 'unassigned_courses': unassigned_courses})

def assign_course(request, student_id):
    if request.method == 'POST':
        course_id = request.POST.get('course')
        course = get_object_or_404(Course, pk=course_id)
        student = get_object_or_404(Student, pk=student_id)
        student.courses.add(course)
        return redirect('course_list', student_id=student_id)
    else:
        unassigned_courses = Course.objects.exclude(student__id=student_id)
        return render(request, 'day2/show_student_info/assign_course.html', {'student_id': student_id, 'unassigned_courses': unassigned_courses})


def homepage(request):
    return render(request, 'day2/home.html')

def courses(request):
    all=Course.objects.all()
    return render(request,"day4/home.html",{'all_courses':all})




def search_student(request):
    student_id = request.GET.get('student_id')
    student = None
    if student_id:
        try:
            student = Student.objects.get(roll=student_id)
        except Student.DoesNotExist:
            pass
    return render(request, 'day2/show_student_info/search_student.html', {'student': student})


def register(request, student_id):
    try:
        student = Student.objects.get(roll=student_id)
    except Student.DoesNotExist:
        return redirect('home')  # Redirect if student with given ID does not exist

    if request.method == 'POST':
        selected_courses_ids = request.POST.getlist('courses')
        selected_courses = Course.objects.filter(id__in=selected_courses_ids)
        student.courses.add(*selected_courses)
        return render(request, 'day2/show_student_info/search_student.html', {'student': student})
    else:
        registered_course_ids = student.courses.values_list('id', flat=True)
        remaining_courses = Course.objects.exclude(id__in=registered_course_ids)
        return render(request, 'day2/show_student_info/registration.html', {'student': student, 'remaining_courses': remaining_courses})


def remove_student(request,id):
    c=Student.objects.get(id=id)
    c.delete()
    return redirect(student_list)

def edit_student(request,id):
    s=Student.objects.get(id=id)
    sfrm = StudentForm(instance=s)
    #print('-----------'+request.method+'------------')
    if request.method=="POST":
        frm = StudentForm(request.POST, instance=s)
        if frm.is_valid():
            frm.save()
        return redirect(student_list)
    return render(request,'day2/show_student_info/edit_stu.html',{'form':sfrm})

def add_student(request):
    frm = StudentForm()
    return render(request,'day2/show_student_info/add_stu.html',{'form':frm})

def save_student(request):
    if request.method == 'POST':
        frm = StudentForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect(student_list)
        else: 
            print("invalid")
    return redirect(student_list)    


def remove_course(request, student_id, course_id):
    student = get_object_or_404(Student, id=student_id)
    course = get_object_or_404(Course, id=course_id)
    
    # Remove the course from the student's courses
    student.courses.remove(course)
    
    return render(request, 'day2/show_student_info/search_student.html', {'student': student})