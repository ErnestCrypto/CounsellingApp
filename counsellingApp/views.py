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
            arr_title = []
            arr_firstname = []
            arr_lastname = []
            arr_user_id = []
            arr_pin = []
            arr_status = []

            for use in user:
                title = use.title
                firstName = use.firstName
                lastname = use.lastName
                user_id = use.user_id
                pin = use.pin
                status = use.status
                arr_title.append(title)
                arr_firstname.append(firstName)
                arr_lastname.append(lastname)
                arr_user_id.append(user_id)
                arr_pin.append(pin)
                arr_status.append(status)

            for u in range(len(arr_user_id)):
                l_title = arr_title[u]
                l_firstname = arr_firstname[u]
                l_lastname = arr_lastname[u]
                l_user = arr_user_id[u]
                l_pin = arr_pin[u]
                l_status = arr_status[u]

                if str(l_user) == str(person_id) and str(l_pin) == str(pin_log) and str(l_status) == str(option):
                    user_id = l_user
                    messages.success(
                        request, f'{l_title} { l_firstname}  {l_lastname} ')
                    obj = login.save(commit=False)
                    obj.person_firstname = l_firstname
                    obj.person_lastname = l_lastname
                    obj.save()
                    return redirect('counsellingUrls:homePage', user_id)

        else:
            messages.error(request, '-- Please check your credentials --')
    return render(request, 'app/login.html', {
        'log': login

    })


def indexPage(request):
    home = 'app/home.html'
    return render(request, 'app/index.html', {'home': home})


def homePage(request, pk):
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

        if achievement.is_valid():
            messages.success(request, f'pk: {pk}')
            # counsellor.save()
            arr_counsellor_id = []
            arr_counsellor_user_id = []

            for object in objects:
                counsellor_id = object.id
                counsellor_user_id = object.user_id
                arr_counsellor_user_id.append(counsellor_user_id)
                arr_counsellor_id.append(counsellor_id)

            for u in range(len(arr_counsellor_id)):
                l_counsellor_user_id = arr_counsellor_user_id[u]
                l_counsellor_id = arr_counsellor_id[u]

                if str(l_counsellor_user_id) == str(pk):
                    ach_obj = achievement.save(commit=False)
                    avail_obj = availability.save(commit=False)
                    edu_obj = education.save(commit=False)
                    exp_obj = experience.save(commit=False)
                    ther_obj = therapy.save(commit=False)
                    spec_obj = specialities.save(commit=False)

                    counsellor_inst = Counsellor.objects.get(
                        id=l_counsellor_id)
                    ach_obj.counsellor = counsellor_inst
                    avail_obj.counsellor = counsellor_inst
                    edu_obj.counsellor = counsellor_inst
                    exp_obj.counsellor = counsellor_inst
                    ther_obj.counsellor = counsellor_inst
                    spec_obj.counsellor = counsellor_inst

                    ach_obj.user_id = pk
                    avail_obj.user_id = pk
                    edu_obj.user_id = pk
                    exp_obj.user_id = pk
                    ther_obj.user_id = pk
                    spec_obj.user_id = pk

                    messages.success(request, f'id : {l_counsellor_user_id} ')
                    ach_obj.save()
                    avail_obj.save()
                    edu_obj.save()
                    exp_obj.save()
                    ther_obj.save()
                    spec_obj.save()

            # firstname = counsellor.cleaned_data['firstName']
            # lastname = counsellor.cleaned_data['lastName']

            messages.success(
                request, f'Your account has been created successfully.')

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
                                             'Counsellor': counsellor,
                                             'objects': objects,
                                             'pk': pk,



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
