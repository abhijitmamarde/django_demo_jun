from django.http import HttpResponse

def hello(request):
    return HttpResponse("<b>Hello World. Welcome to Django</b>")
