# creating views
from audioop import reverse
from django.http import request
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Counsellor, SuperCounsellor, Achievement, Availability, Education, Experience, Therapy, Specialities, Login
from .forms import CounsellorForm, SuperCounsellorForm, AchievementForm, AvailabilityForm, EducationForm, ExperienceForm, TherapyForm, SpecialitiesForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def loginPage(request):
    login = LoginForm()

    if request.method == "POST":
        login = LoginForm(request.POST)
        person_id = request.POST.get('person_id')
        pin_log = request.POST.get('pin_log')
        option = request.POST.get('option')
        user = Counsellor.objects.all()
        if login.is_valid():
            messages.success(request, 'Welcome to UGCounselling')
            arr_user_id = []
            arr_pin = []
            arr_status = []

            for use in user:
                user_id = use.user_id
                pin = use.pin
                status = use.status
                arr_user_id.append(user_id)
                arr_pin.append(pin)
                arr_status.append(status)

            for u in range(len(arr_user_id)):
                l_user = arr_user_id[u]
                l_pin = arr_pin[u]
                l_status = arr_status[u]
                if str(l_user) == str(person_id) and str(l_pin) == str(pin_log) and str(l_status) == str(option):
                    login.save()
                    # return redirect('/home/')
        else:
            messages.error(request, '-- Please check your credentials --')

    return render(request, 'app/login.html', {
        'log': login

    })


def indexPage(request):
    home = 'app/home.html'
    return render(request, 'app/index.html', {'home': home})


@login_required
def homePage(request):
    admin = 'app/admin.html'
    profile = 'app/profile.html'
    notification = 'app/notification.html'
    index = 'app/index.html'
    counsellor = CounsellorForm()
    achievement = AchievementForm()
    availability = AvailabilityForm()
    education = EducationForm()
    experience = ExperienceForm()
    therapy = TherapyForm()
    specialities = SpecialitiesForm()
    Supercounselloform = SuperCounsellorForm()
    objects = Counsellor.objects.all()

    if request.method == 'POST':

        counsellor = CounsellorForm(request.POST, request.FILES)
        achievement = AchievementForm(request.POST)
        availability = AvailabilityForm(request.POST)
        education = EducationForm(request.POST)
        experience = ExperienceForm(request.POST)
        therapy = TherapyForm(request.POST)
        specialities = SpecialitiesForm(request.POST)
        Supercounselloform = SuperCounsellorForm(request.POST)

        if counsellor.is_valid():
            counsellor.save()
            achievement.save()
            availability.save()
            education .save()
            experience.save()
            therapy .save()
            specialities.save()
            firstname = counsellor.cleaned_data['firstName']
            lastname = counsellor.cleaned_data['lastName']

            messages.success(
                request, f'Hi {firstname} {lastname} your account has been created successfully.')

        else:
            counsellor = CounsellorForm()
            achievement = AchievementForm()
            availability = AvailabilityForm()
            education = EducationForm()
            experience = ExperienceForm()
            therapy = TherapyForm()
            specialities = SpecialitiesForm()

            messages.error(
                request, 'Failed to create your account, please check your details')

    return render(request, 'app/home.html', {'profile': profile,
                                             'notification': notification,
                                             'index': index,
                                             'admin': admin,
                                             'counsellor':  counsellor,
                                             'achievement': achievement,
                                             'availability': availability,
                                             'education': education,
                                             'experience': experience,
                                             'therapy': therapy,
                                             'specialities': specialities,
                                             'Counsellor': objects,

                                             })


def adminPage(request):
    admin = 'app/admin.html'
    settings = 'app/settings.html'
    dashboard = 'app/dashboard.html'

    return render(request, 'app/admin.html', {
        'admins': admin,
        'settings': settings,
        'dashboard': dashboard,
    })


def profilePage(request):
    return render(request, 'app/profile.html', {})


def dashboardPage(request):

    # achievement = AchievemenetForm()
    # availability = AvailabilityForm()

    return render(request, 'app/dashboard.html', {})
