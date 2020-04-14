from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url('process', views.process, name='process')]
