# creating views
from audioop import reverse
from django.http import request
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Counsellor, SuperCounsellor, Achievement, Availability, Education, Experience, Therapy, Specialities, Login, Bookings, Meetings
from .forms import CounsellorForm, SuperCounsellorForm, AchievementForm, AvailabilityForm, EducationForm, ExperienceForm, TherapyForm, SpecialitiesForm, LoginForm, BookingsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .serializers import CounsellorSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
import calendar
from calendar import HTMLCalendar


def test(request):
    return render(request, 'test.html', {})


@api_view(['GET', 'PUT', 'DELETE'])
def Counsellor_details(request, pk):
    try:
        counsellor = Counsellor.objects.get(user_id=pk)
    except counsellor.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = CounsellorSerializer(counsellor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CounsellorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        counsellor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def Counsellor_list(request):
    if request.method == 'GET':
        counsellor = Counsellor.objects.all()
        serializer = CounsellorSerializer(counsellor, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CounsellorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def loginPage(request):
    login = LoginForm()

    if request.method == "POST":
        login = LoginForm(request.POST)
        person_id = request.POST.get('person_id')
        pin_log = request.POST.get('pin_log')
        option = request.POST.get('option')
        request.session['option'] = option

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

                    request.session['pk'] = user_id
                    return redirect('counsellingUrls:indexPage', user_id)

        else:
            messages.error(request, '-- Please check your credentials --')
    return render(request, 'app/login.html', {
        'log': login

    })


def superadminPage(request, pk):
    objects = Counsellor.objects.all()
    count = Counsellor.objects.all().count()
    bookcount = Bookings.objects.filter(counsellor_user_id=pk).count()
    meetingcount = Meetings.objects.filter(counsellor_user_id=pk).count()
    bookings = Bookings.objects.all().count()
    meetings = Meetings.objects.all().count()
    request.session['pk'] = pk

    return render(request, 'app/super.html', {
        'objects': objects,
        'pk': pk,
        'count': count,
        'bookings': bookings,
        'meetings': meetings,
        'bookcount': bookcount,
        'meetingcount': meetingcount,
    })


def adminPage(request, pk):
    objects = Counsellor.objects.all()
    count = Counsellor.objects.all().count()
    bookcount = Bookings.objects.filter(counsellor_user_id=pk).count()
    meetingcount = Meetings.objects.filter(counsellor_user_id=pk).count()
    bookings = Bookings.objects.all().count()
    meetings = Meetings.objects.all().count()
    request.session['pk'] = pk

    return render(request, 'app/admin.html', {
        'objects': objects,
        'pk': pk,
        'count': count,
        'bookings': bookings,
        'meetings': meetings,
        'bookcount': bookcount,
        'meetingcount': meetingcount,
    })


def calender(request):
    return render(request, 'admin/events/change_list.html', {})


def availiablePage(request, pk):
    pk = request.session['pk']

    return render(request, 'app/availiable.html', {
        'pk': pk,
        'range': range(8),
        'rang': range(10),

    })


def homePage(request, pk):

    request.session['pk'] = pk
    objects = Counsellor.objects.all()

    return render(request, 'app/home.html', {
        'objects': objects,
        'pk': pk,

    }

    )


def dashboardPage(request, pk):
    admin = 'app/admin.html'
    profile = 'app/profile.html'
    notification = 'app/notification.html'
    index = 'app/index.html'
    counsellor = CounsellorForm()
    achieve = Achievement.objects.all()
    edu = Education.objects.all()
    expe = Experience.objects.all()
    ther = Therapy.objects.all()
    spec = Specialities.objects.all()
    achievement = AchievementForm()
    education = EducationForm()
    experience = ExperienceForm()
    therapy = TherapyForm()
    books = BookingsForm()
    specialities = SpecialitiesForm()
    Supercounsellorform = SuperCounsellorForm()
    objects = Counsellor.objects.all()
    obj_ach = Achievement.objects.all()
    obj_avai = Availability.objects.all()
    obj_exp = Experience.objects.all()
    obj_the = Therapy.objects.all()
    obj_spe = Specialities.objects.all()
    count = Counsellor.objects.all().count()
    bookcount = Bookings.objects.filter(counsellor_user_id=pk).count()
    meetingcount = Meetings.objects.filter(counsellor_user_id=pk).count()
    bookings = Bookings.objects.all().count()
    meetings = Meetings.objects.all().count()
    request.session['pk'] = pk
    studentbooks = Bookings.objects.all()
    avaibooks = Availability.objects.all()

    for object in objects:
        if str(object.user_id) == str(pk):
            counsellor = CounsellorForm(initial={
                'user_id': object.user_id,
                'pin': object.pin,
                'firstName': object.firstName,
                'lastName': object.lastName,
                'email': object.email,
                'title': object.title,
                'gender': object.gender,
                'about': object.about,
                'contact': object.contact,
                'occupation': object.occupation,

            })

    if request.method == 'POST':

        books = BookingsForm(request.POST)
        coun = Counsellor.objects.get(user_id=pk)
        counsellor = CounsellorForm(request.POST, request.FILES, instance=coun)
        achievement = AchievementForm(request.POST)
        education = EducationForm(request.POST)
        experience = ExperienceForm(request.POST)
        therapy = TherapyForm(request.POST)
        specialities = SpecialitiesForm(request.POST)
        Supercounsellorform = SuperCounsellorForm(request.POST)

        if books.is_valid():
            messages.success(request, 'Booking recorded successfully')
            bsave = books.save(commit=False)
            bsave.cousellor_user_id = pk
            bsave.save()

        if counsellor.is_valid():
            counsellor.save()
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
            arr_counsellor_profile = []

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
                counsellor_profile = object.profile
                arr_counsellor_profile.append(counsellor_profile)
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
                l_counsellor_profile = arr_counsellor_profile[u]
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

                    # coun.user_id = pk
                    # coun.about = l_counsellor_about
                    # coun.title = l_counsellor_title
                    # coun.firstName = l_counsellor_firstname
                    # coun.lastName = l_counsellor_lastname
                    # coun.gender = l_counsellor_gender
                    # coun.occupation = l_counsellor_occupation
                    # coun.contact = l_counsellor_contact
                    # coun.email = l_counsellor_email
                    # coun.profile = l_counsellor_profile

                    ach_obj = achievement.save(commit=False)
                    edu_obj = education.save(commit=False)
                    exp_obj = experience.save(commit=False)
                    ther_obj = therapy.save(commit=False)
                    spec_obj = specialities.save(commit=False)
                    counsellor_inst = Counsellor.objects.get(
                        id=l_counsellor_id)

                    ach_obj.counsellor = counsellor_inst
                    edu_obj.counsellor = counsellor_inst
                    exp_obj.counsellor = counsellor_inst
                    ther_obj.counsellor = counsellor_inst
                    spec_obj.counsellor = counsellor_inst

                    ach_obj.user_id = pk
                    edu_obj.user_id = pk
                    exp_obj.user_id = pk
                    ther_obj.user_id = pk
                    spec_obj.user_id = pk

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

    return render(request, 'app/dashboard.html', {'profile': profile,
                                                  'notification': notification,
                                                  'index': index,
                                                  'admin': admin,
                                                  'counsellor':  counsellor,
                                                  'achievement': achievement,
                                                  'education': education,
                                                  'experience': experience,
                                                  'therapy': therapy,
                                                  'specialities': specialities,
                                                  'Counsellor': counsellor,
                                                  'objects': objects,
                                                  'pk': pk,
                                                  'obj_ach': obj_ach,
                                                  'obj_avai': obj_avai,
                                                  'obj_exp': obj_exp,
                                                  'obj_the': obj_the,
                                                  'obj_spe': obj_spe,
                                                  'count': count,
                                                  'books': books,
                                                  'bookings': bookings,
                                                  'meetings': meetings,
                                                  'studentbooks': studentbooks,
                                                  'avaibooks': avaibooks,
                                                  'bookcount': bookcount,
                                                  'meetingcount': meetingcount,
                                                  'achieve': achieve,
                                                  'edu': edu,
                                                  'expe': expe,
                                                  'ther': ther,
                                                  'spec': spec,

                                                  }

                  )


def settingsPage(request, pk):
    objects = Counsellor.objects.all()
    request.session['pk'] = pk
    studentbooks = Bookings.objects.all()

    return render(request, 'app/settings.html', {
        'objects': objects,
        'pk': pk,
        'studentbooks': studentbooks,

    }

    )


def indexPage(request, pk):
    objects = Counsellor.objects.all()
    request.session['pk'] = pk

    return render(request, 'app/index.html', {
        'objects': objects,
        'pk': pk,
    })


def popupPage(request, object_user_id):
    objects = Counsellor.objects.all()
    pk = request.session['pk']
    user_id = object_user_id

    return render(request, 'app/popup.html', {
        'objects': objects,
        'pk': pk,
        'user_id': user_id,
    })


def notificationPage(request, pk):
    objects = Counsellor.objects.all()
    request.session['pk'] = pk

    return render(request, 'app/notification.html', {
        'objects': objects,
        'pk': pk,
    })


def profilePage(request, pk):
    objects = Counsellor.objects.all()
    obj_ach = Achievement.objects.all()
    obj_avai = Availability.objects.all()
    obj_exp = Experience.objects.all()
    obj_the = Therapy.objects.all()
    obj_spe = Specialities.objects.all()
    request.session['pk'] = pk

    return render(request, 'app/profile.html', {

        'objects': objects,
        'pk': pk,
        'obj_ach': obj_ach,
        'obj_avai': obj_avai,
        'obj_exp': obj_exp,
        'obj_the': obj_the,
        'obj_spe': obj_spe,

    })


def search(request, pk):
    pk = request.session['pk']
    search = ''

    if request.method == 'GET':
        search = request.GET.get('search')
        post = Counsellor.objects.all()
        if search:
            search = request.GET.get('search').split(' ')
            for u in range(len(search)):
                l_search = search[u]

                post = Counsellor.objects.filter(
                    Q(firstName__icontains=l_search) | Q(lastName__icontains=l_search))

        else:
            search = ''
        pk = request.session['pk']
        return render(request, 'app/result.html', {
            'post': post,
            'search': search,
            'pk': pk,

        })
    return redirect('counsellingUrls:profilePage', pk)


def delete(request, studentbook_id):
    pk = request.session['pk']
    book = Bookings.objects.get(id=studentbook_id)
    book.delete()
    return redirect('counsellingUrls:settingsPage', pk)


def update(request, studentbook_id, studentbook_status):
    pk = request.session['pk']
    book_id = Bookings.objects.get(id=studentbook_id)
    books = BookingsForm(instance=book_id)

    if str(studentbook_status) == 'Pending':
        booksave = books.save(commit=False)
        booksave.student_status = 'Approved'
        booksave.save()
        messages.success(request, 'approved')
    elif str(studentbook_status) == 'Approved':
        booksave = books.save(commit=False)
        booksave.student_status = 'Pending'
        booksave.save()
        messages.success(request, 'pending')

    return redirect('counsellingUrls:settingsPage', pk)


def achievement_add(request, ach_id):
    pk = request.session['pk']
    achieve = Achievement.objects.get_or_create(id=ach_id)
    messages.success(request, f'{achieve}')

    
    return redirect('counsellingUrls:dashboardPage', pk)


def achievement_del(request, ach_id):
    pk = request.session['pk']
    achieve = Achievement.objects.get(id=ach_id)
    achieve.delete()
    return redirect('counsellingUrls:dashboardPage', pk)


def education_add(request, ed_id):
    pk = request.session['pk']

    return redirect('counsellingUrls:dashboardPage', pk)


def education_del(request, ed_id):
    pk = request.session['pk']
    edu = Education.objects.get(id=ed_id)
    edu.delete()
    return redirect('counsellingUrls:dashboardPage', pk)


def experience_add(request, exp_id):
    pk = request.session['pk']

    return redirect('counsellingUrls:dashboardPage', pk)


def experience_del(request, exp_id):
    pk = request.session['pk']
    expe = Experience.objects.get(id=exp_id)
    expe.delete()
    return redirect('counsellingUrls:dashboardPage', pk)


def therapy_add(request, the_id):
    pk = request.session['pk']

    return redirect('counsellingUrls:dashboardPage', pk)


def therapy_del(request, the_id):
    pk = request.session['pk']
    ther = Therapy.objects.create(id=the_id)
    ther.delete()
    return redirect('counsellingUrls:dashboardPage', pk)


def speciality_add(request, spe_id):
    pk = request.session['pk']

    return redirect('counsellingUrls:dashboardPage', pk)


def speciality_del(request, spe_id):
    pk = request.session['pk']
    spec = Specialities.objects.get(id=spe_id)
    spec.delete()
    return redirect('counsellingUrls:dashboardPage', pk)
