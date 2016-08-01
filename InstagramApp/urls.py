from django.conf.urls import url,patterns,include
from InstagramApp import views
from django.conf.urls import patterns, include, url
from InstagramApp.views import *

urlpatterns = [
    url(r'add?$',views.create_View.as_view(),name="list"),
    url(r'^$',views.class_View.as_view(),name="imageList"),
]