from django.shortcuts import render
from .import views

# Create your views here.
def index(request):
    context={}
    return render(request,'autotech/index.html',context)