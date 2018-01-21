
from django.conf.urls import url
from django.contrib import admin
from university import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^teacher/(?P<teacher_id>\d+)', views.single_teacher, name='single_teacher'),
    url(r'^faculty/(?P<faculty_name>\w+)', views.faculty_info, name='faculty_info'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^signup/', views.signup, name='signup')

]
