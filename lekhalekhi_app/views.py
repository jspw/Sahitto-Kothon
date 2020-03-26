from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

##
app_name = 'lekhalekhi'

def index(request):
    dist = {'title':'সাহিত্যকথন'}
    return render(request,'lekhalekhi_app/home.html',dist)