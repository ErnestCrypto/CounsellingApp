# creating views
from django.http import request
from django.shortcuts import render


def homePage(request):
    context = {}
    return render(request, 'app/home.html', {})
