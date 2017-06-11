from django.conf.urls import url
from django.http import HttpResponse
from .models import Student, CommonFields

from django.shortcuts import render
from django import forms

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

def list_student(request):
    students = Student.objects.all()
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

    students = Student.objects.all()
    return render(request, "list_student.html", dict(students=students))


urlpatterns = [
    url(r'^list$', list_student),
    url(r'^show/(\d+)$', show_student),
    url(r'^add$', add_student),
    url(r'^addnew$', add_student_handler),
]
