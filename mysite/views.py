from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print("bye")
    return render(request,'home.html')
