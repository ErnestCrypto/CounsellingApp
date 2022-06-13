from django.shortcuts import render, redirect
from counsellingApp.models import Counsellor, Students, Availability, Bookings
from counsellingApp.forms import BookingsForm
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.conf import settings


def index(request, pk):
    request.session['pk'] = pk
    students = Students.objects.all()
    counsellors = Counsellor.objects.all()
    return render(request, 'index.html', {
        'pk': pk,
        'students': students,
        'counsellors': counsellors,
    })


def about(request):
    pk = request.session['pk']
    students = Students.objects.all()
    counsellors = Counsellor.objects.all()
    return render(request, 'about.html', {
        'pk': pk,
        'students': students,
        'counsellors': counsellors,
    })


def blog_single(request):
    pk = request.session['pk']
    students = Students.objects.all()
    counsellors = Counsellor.objects.all()
    return render(request, 'blog-single.html', {
        'pk': pk,
        'students': students,
        'counsellors': counsellors,
    })


def blog(request):
    pk = request.session['pk']
    students = Students.objects.all()
    counsellors = Counsellor.objects.all()
    return render(request, 'blog.html', {
        'pk': pk,
        'students': students,
        'counsellors': counsellors,

    })


def contact(request):
    pk = request.session['pk']
    students = Students.objects.all()
    counsellors = Counsellor.objects.all()
    return render(request, 'contact.html', {
        'pk': pk,
        'students': students,
        'counsellors': counsellors,
    })


def counselor(request):
    objects = Counsellor.objects.all()
    pk = request.session['pk']
    students = Students.objects.all()
    counsellors = Counsellor.objects.all()
    return render(request, 'counselor.html', {
        'objects': objects,
        'pk': pk,
        'students': students,
        'counsellors': counsellors,
    })


def details(request, object_id):
    objects = Counsellor.objects.all()
    counselor = object_id
    pk = request.session['pk']
    students = Students.objects.all()
    coun = Counsellor.objects.get(user_id=object_id)
    availables = Availability.objects.filter(counsellor=coun)
    counsellors = Counsellor.objects.all()
    return render(request, 'details.html', {
        'objects': objects,
        'counselor': counselor,
        'pk': pk,
        'students': students,
        'availables': availables,
        'counsellors': counsellors,
    })


def services(request):
    pk = request.session['pk']
    students = Students.objects.all()
    counsellors = Counsellor.objects.all()
    return render(request, 'services.html', {
        'pk': pk,
        'students': students,
        'counsellors': counsellors,
    })


def logout(request, pk):
    return redirect('counsellingUrls:loginPage')


def send(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_input = request.POST.get('email')
        msg = request.POST.get('msg')
        subject = request.POST.get('subject')
        message = f'NAME: {name}, EMAIL: {email_input}, SERVICE: {subject}, MESSAGE: {msg}'

        send_mail(
            'contact form',
            message,
            settings.EMAIL_HOST_USER,
            ['itservices@ug.edu.gh'],
            fail_silently=False,

        )

        # email = EmailMessage(
        #     f'Mail',  # subject
        #     f'Name: {name}, Email: {email_input}, Message: {msg}, Service: {services}',
        #     settings.EMAIL_HOST_USER,  # sender email
        #     ['itservices@ug.edu.gh'],  # receiver email
        # )

        # email.fail_silently = True
        # email.send()

        return render(request, 'sent.html', {
            'pk': pk,
        })


def book(request, pk, object_user_id):

    counsellor = Counsellor.objects.get(user_id=object_user_id)
    student = Students.objects.get(student_id=pk)

    stud_name = student.firstName + ' ' + student.lastName

    if request.method == 'POST':
        book = BookingsForm(request.POST)
        if book.is_valid():
            book = book.save(commit=False)
            book.counsellor = counsellor
            book.counsellor_user_id = counsellor.user_id
            book.student_id = student.student_id
            book.student_name = stud_name
            book.save()

    return render(request, 'book.html', {
        'pk': pk,
    })
