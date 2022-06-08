from django.shortcuts import render


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
    return render(request, 'counselor.html', {})


def services(request):
    return render(request, 'services.html', {})
