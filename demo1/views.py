from django.http import HttpResponse

def hello(request):
    return HttpResponse("<b>Hello World V2. Welcome to Django</b>")
