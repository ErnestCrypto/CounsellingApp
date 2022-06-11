from django.shortcuts import render, redirect
from counsellingApp.models import Counsellor, Students
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings


def index(request, pk):
    request.session['pk'] = pk
    students = Students.objects.all()
    return render(request, 'index.html', {
        'pk': pk,
        'students': students,
    })


def about(request):
    pk = request.session['pk']
    students = Students.objects.all()
    return render(request, 'about.html', {
        'pk': pk,
        'students': students,
    })


def blog_single(request):
    pk = request.session['pk']
    students = Students.objects.all()
    return render(request, 'blog-single.html', {
        'pk': pk,
        'students': students,
    })


def blog(request):
    pk = request.session['pk']
    students = Students.objects.all()
    return render(request, 'blog.html', {
        'pk': pk,
        'students': students,
    })


def contact(request):
    pk = request.session['pk']
    students = Students.objects.all()
    return render(request, 'contact.html', {
        'pk': pk,
        'students': students,
    })


def counselor(request):
    objects = Counsellor.objects.all()
    pk = request.session['pk']
    students = Students.objects.all()
    return render(request, 'counselor.html', {
        'objects': objects,
        'pk': pk,
        'students': students,
    })


def details(request, object_id):
    objects = Counsellor.objects.all()
    counselor = object_id
    pk = request.session['pk']
    students = Students.objects.all()
    return render(request, 'details.html', {
        'objects': objects,
        'counselor': counselor,
        'pk': pk,
        'students': students,
    })


def services(request):
    pk = request.session['pk']
    students = Students.objects.all()
    return render(request, 'services.html', {
        'pk': pk,
        'students': students,
    })


def logout(request, pk):
    return redirect('counsellingUrls:loginPage')


def send(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_input = request.POST.get('email')
        msg = request.POST.get('msg')
        services = request.POST.get('services')
        email = EmailMessage(
            f'Mail',  # subject
            f'Name: {name}, Email: {email_input}, Message: {msg}, Service: {services}',
            settings.EMAIL_HOST_USER,  # sender email
            ['itservices@ug.edu.gh'],  # receiver email
        )

        email.fail_silently = True
        email.send()

        return render(request, 'sent.html', {
            'pk': pk,
        })
