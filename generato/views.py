from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generato/home.html')
    
def about(request):
    return render(request, 'generato/about.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('*&^%$@!#'))

    if request.GET.get('numbers'):
            characters.extend(list('123456'))



    length= int(request.GET.get('length',12))

    thepassword =''
    for x in range (length):
        thepassword += random.choice(characters)


    return render(request, 'generato/password.html', {'password':thepassword})
