from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def padonak(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+{}|?><:=-'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    lenght = int(request.GET.get('lenght', 12))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/padonak.html', {'padonak':thepassword})

def about(request):
    return render(request, 'generator/about.html')