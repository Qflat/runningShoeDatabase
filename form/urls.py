from django.conf.urls import url
from .views import ShoeForm

urlpatterns = [
    url('', ShoeForm.as_view(), name='ShoeForm'),
    #url('process', views.process, name='process'),
    ]
