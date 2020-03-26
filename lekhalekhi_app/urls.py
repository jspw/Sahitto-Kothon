from django.conf.urls import url
from lekhalekhi_app import  views

urlpatterns = [
    url(r'^$',views.index,name='index')
]
