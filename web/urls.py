from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit/Available_Public_IP/$', views.submit_Available_Public_IP, name='Submit_Available_Public_IP'),
    url(r'^submit/Used_Public_IP/$', views.submit_Used_Public_IP, name='Submit_Used_Public_IP'),
    url(r'^submit/Used_Private_IP/$', views.submit_Used_Private_IP, name='Submit_Used_Private_IP'),
]