from django.shortcuts import render
from counsellingApp.models import Counsellor
from django.contrib import messages


def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def blog_single(request):
    return render(request, 'blog-single.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def counselor(request):
    objects = Counsellor.objects.all()
    return render(request, 'counselor.html', {
        'objects': objects,
    })


def details(request, object_id):
    objects = Counsellor.objects.all()
    counselor = object_id

    return render(request, 'details.html', {
        'objects': objects,
        'counselor': counselor,
    })


def services(request):
    return render(request, 'services.html', {})
