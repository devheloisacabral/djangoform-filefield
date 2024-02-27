from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
from .models import modelfield


from project import settings


# Create your views here.

def home(request):
    if request.method == 'POST':
        file = request.FILES.get('file')

        myfile = modelfield(title='file', doc=file)
        myfile.save()
        return HttpResponse("STATUS 200. OK!")

    elif request.method == 'GET':
        return render(request, 'home.html')
