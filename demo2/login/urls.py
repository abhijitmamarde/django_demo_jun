from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.shortcuts import render

def home_page(request):
    username = None
    is_logged = request.user.is_authenticated()
    if request.user.is_authenticated():
        username = request.user.username

    return render(request, "home.html", dict(username=username, 
        is_logged=is_logged))

    # return HttpResponse('''
    # <h3>Welcome to HOME page</h3>
    # <p>You are logged in as: %(name)s</p>
    # ''' % dict(
    #     name=username
    # ))

urlpatterns = [
    url(r'^login/$', auth_views.login,   {'template_name': 'login.html'}, name='login'),
    # url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='logout'),

    url(r'^home/$', home_page, name='home'),
]