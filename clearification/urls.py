from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<contest_name>[^/]+)/$', views.clearification, name='clearification'),
]