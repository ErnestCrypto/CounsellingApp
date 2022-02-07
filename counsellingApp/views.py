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
            arr_user_id = []
            messages.success(request, 'Welcome to UGCounselling')

            for use in user:
                user_id = use.user_id
                pin = use.pin
                status = use.status
                arr_user_id = user_id

            if arr_user_id == person_id:
                login.save()

            else:
                messages.error(request, '-- This account does not exist --')

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
