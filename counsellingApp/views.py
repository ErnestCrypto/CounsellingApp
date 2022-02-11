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
    Supercounsellorform = SuperCounsellorForm()
    objects = Counsellor.objects.all()

    if request.method == 'POST':

        coun = Counsellor.objects.get(user_id=pk)
        counsellor = CounsellorForm(request.POST, instance=coun)
        achievement = AchievementForm(request.POST)
        availability = AvailabilityForm(request.POST)
        education = EducationForm(request.POST)
        experience = ExperienceForm(request.POST)
        therapy = TherapyForm(request.POST)
        specialities = SpecialitiesForm(request.POST)
        Supercounsellorform = SuperCounsellorForm(request.POST)

        if counsellor.is_valid():
            counsellor.save()
            messages.success(request, f'pk: {pk}')
            arr_counsellor_id = []
            arr_counsellor_pin = []
            arr_counsellor_user_id = []
            arr_counsellor_firstname = []
            arr_counsellor_lastname = []
            arr_counsellor_title = []
            arr_counsellor_email = []
            arr_counsellor_email = []
            arr_counsellor_gender = []
            arr_counsellor_occupation = []
            arr_counsellor_about = []
            arr_counsellor_contact = []

            for object in objects:
                counsellor_id = object.id
                counsellor_pin = object.pin
                counsellor_user_id = object.user_id
                counsellor_firstname = object.firstName
                counsellor_lastname = object.lastName
                counsellor_title = object.title
                counsellor_gender = object.gender
                counsellor_about = object.about
                counsellor_email = object.email
                counsellor_contact = object.contact
                counsellor_occupation = object.occupation
                arr_counsellor_id.append(counsellor_id)
                arr_counsellor_pin.append(counsellor_pin)
                arr_counsellor_user_id.append(counsellor_user_id)
                arr_counsellor_firstname.append(counsellor_firstname)
                arr_counsellor_lastname.append(counsellor_lastname)
                arr_counsellor_title.append(counsellor_title)
                arr_counsellor_gender.append(counsellor_gender)
                arr_counsellor_about.append(counsellor_about)
                arr_counsellor_email.append(counsellor_email)
                arr_counsellor_contact.append(counsellor_contact)
                arr_counsellor_occupation.append(counsellor_occupation)

            for u in range(len(arr_counsellor_id)):
                l_counsellor_user_id = arr_counsellor_user_id[u]
                l_counsellor_id = arr_counsellor_id[u]
                l_counsellor_pin = arr_counsellor_pin[u]
                l_counsellor_firstname = arr_counsellor_firstname[u]
                l_counsellor_lastname = arr_counsellor_lastname[u]
                l_counsellor_title = arr_counsellor_title[u]
                l_counsellor_gender = arr_counsellor_gender[u]
                l_counsellor_about = arr_counsellor_about[u]
                l_counsellor_email = arr_counsellor_email[u]
                l_counsellor_contact = arr_counsellor_contact[u]
                l_counsellor_occupation = arr_counsellor_occupation[u]

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

                    messages.success(
                        request, f'id : {l_counsellor_user_id} ')
                    # counsellor = CounsellorForm(initial={
                    #     'user_id': l_counsellor_user_id,
                    #     'firstName': str(l_counsellor_firstname),
                    #     'lastName': str(l_counsellor_lastname),
                    #     'email': l_counsellor_email,
                    #     'title': l_counsellor_title,
                    #     'gender': l_counsellor_gender,
                    #     'about': l_counsellor_about,
                    #     'contact': l_counsellor_contact,
                    #     'occupation': l_counsellor_occupation,
                    # })
                    ach_obj.save()
                    avail_obj.save()
                    edu_obj.save()
                    exp_obj.save()
                    ther_obj.save()
                    spec_obj.save()

            # firstname = counsellor.cleaned_data['firstName']
            # lastname = counsellor.cleaned_data['lastName']

            messages.success(
                request, 'Your account has been updated successfully.')

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
