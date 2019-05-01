from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit/Available_Public_IP/$', views.submit_Available_Public_IP, name='Submit_Available_Public_IP')
]