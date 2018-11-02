from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^index/$',views.index),
    url('^info/$',views.info),
    url('^createstudent/$',views.createstudent),
]
