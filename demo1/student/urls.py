from django.conf.urls import url

from django.http import HttpResponse

from .models import Student, CommonFields


# from django import forms

# class StudentAddForm(forms.ModelForm):

#     class Meta:
#         model = Student
#         fields = ('first_name', 'last_name')

def add_student(request):
    # form = StudentAddForm()
    output = ["<b>This is add Student page</b>"]
    output.append(' ')

    return HttpResponse("\n".join(output))

def list_student(request):
    output = ["<b>This is list Student page</b>", "<ul>"]

    for student in Student.objects.all():
        output.append('<li>%s %s</li>' % (student.first_name, student.last_name) )

    output.append("</ul>")
    
    return HttpResponse("\n".join(output))

def show_student(request, student_id):
    student_id = int(student_id)
    output = ["<b>This is show Student page for student id:%d</b>" % student_id]
    output.append("<p>Student is:</p>")
    output.append("<p>" + str(Student.objects.filter(id=student_id)[0]) + "</p>")
    return HttpResponse("\n".join(output))


urlpatterns = [
    url(r'^list$', list_student),
    url(r'^show/(\d+)$', show_student),
    url(r'^add$', add_student),
]
