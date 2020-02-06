from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(req):
    return render(req, 'generator/home.html')


def password(req):
    char = list('abcdefghijklmnopqrstuvwxyz')

    if req.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWQYZ'))
    if req.GET.get('special'):
        char.extend(list('!@#£$%^&*()'))
    if req.GET.get('numbers'):
        char.extend(list('1234567890'))

    length = int(req.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(char)

    return render(req, 'generator/password.html', {'password':thepassword})


def about(req):
    return render(req, 'generator/about.html')
