'''
Student application's urls and views functions
'''

from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from .models import Student

class StudentAddForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name')

def add_student(request):
    form = StudentAddForm()
    # output = ["<b>This is add Student page</b>"]
    # output.append(' ')

    # return HttpResponse("\n".join(output))
    return render(request, "add_student.html", dict(form=form))

def edit_student(request, student_id):
    student_id = int(student_id)
    student = Student.objects.filter(id=student_id)[0]

    form = StudentAddForm(instance=student)
    
    return render(request, "edit_student.html", dict(form=form, student=student))

def list_student(request):
    students = Student.objects.all().order_by('last_name')
    return render(request, "list_student.html", dict(students=students))

def show_student(request, student_id):
    student_id = int(student_id)
    student = Student.objects.filter(id=student_id)[0]
    return render(request, "show_student.html", dict(student_id=student_id, student=student))

def add_student_handler(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    s = Student(first_name = first_name, last_name = last_name)
    s.save()
    # return render(request, "add_student_success.html", dict(student=s))

    return list_student(request)

def edit_student_submit_handler(request, student_id):
    student_id = int(student_id)
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    # s = Student(first_name = first_name, last_name = last_name)
    s = Student.objects.filter(id=student_id)[0]
    s.first_name = first_name
    s.last_name = last_name
    s.save()

    return list_student(request)

def delete_student(request, student_id):
    student_id = int(student_id)
    s = Student.objects.filter(id=student_id)[0]
    s.delete()
    # return list_student(request)
    return redirect("/student/list")

urlpatterns = [
    # index page for student
    url(r'$', list_student, name="student_index"),
    url(r'^list$', list_student),
    url(r'^show/(\d+)$', show_student),
    url(r'^add$', add_student),
    url(r'^edit/(\d+)$', edit_student),
    url(r'^edit_student_submit/(\d+)$', edit_student_submit_handler),
    url(r'^add_student_submit$', add_student_handler),
    url(r'^delete/(\d+)$', delete_student),
    
]
