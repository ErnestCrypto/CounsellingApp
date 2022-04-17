# creating views
from audioop import reverse
from django import views
from django.http import request
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Counsellor, SuperCounsellor, Achievement, Availability, Education, Experience, Therapy, Specialities, Login, Bookings, Meetings, Students, Notifications
from .forms import CounsellorForm, SuperCounsellorForm, AchievementForm, AvailabilityForm, EducationForm, ExperienceForm, TherapyForm, SpecialitiesForm, LoginForm, BookingsForm, NotificationsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q
import calendar
from calendar import HTMLCalendar
from django.core.mail import send_mail
from django.core import mail


def test(request):
    return render(request, 'test.html', {})


def loginPage(request):
    login = LoginForm()

    if request.method == "POST":
        login = LoginForm(request.POST)
        person_id = request.POST.get('person_id')
        pin_log = request.POST.get('pin_log')

        user = Counsellor.objects.all()
        student = Students.objects.all()

        if login.is_valid():
            messages.success(request, 'Welcome to UGCounselling')
            arr_title = []
            arr_firstname = []
            arr_lastname = []
            arr_user_id = []
            arr_pin = []
            arr_status = []

            arr_firstname_student = []
            arr_lastname_student = []
            arr_user_id_student = []
            arr_pin_student = []
            arr_status_student = []

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

            for stud in student:
                firstName_student = stud.firstName
                lastname_student = stud.lastName
                user_id_student = stud.student_id
                pin_student = stud.pin
                status_student = stud.status
                arr_firstname_student.append(firstName_student)
                arr_lastname_student.append(lastname_student)
                arr_user_id_student.append(user_id_student)
                arr_pin_student.append(pin_student)
                arr_status_student.append(status_student)

            for u in range(len(arr_user_id)):
                l_title = arr_title[u]
                l_firstname = arr_firstname[u]
                l_lastname = arr_lastname[u]
                l_user = arr_user_id[u]
                l_pin = arr_pin[u]
                l_status = arr_status[u]

                if str(l_user) == str(person_id) and str(l_pin) == str(pin_log):
                    user_id = l_user
                    messages.success(
                        request, f'{l_title} { l_firstname}  {l_lastname} ')
                    obj = login.save(commit=False)
                    obj.person_firstname = l_firstname
                    obj.person_lastname = l_lastname
                    obj.option = l_status
                    obj.save()

                    request.session['pk'] = user_id
                    request.session['counsellor'] = l_lastname
                    return redirect('counsellingUrls:indexPage', user_id)

            for u in range(len(arr_user_id_student)):

                l_firstname_student = arr_firstname_student[u]
                l_lastname_student = arr_lastname_student[u]
                l_user_student = arr_user_id_student[u]
                l_pin_student = arr_pin_student[u]
                l_status_student = arr_status_student[u]

                if str(l_user_student) == str(person_id) and str(l_pin_student) == str(pin_log):
                    user_id_student = l_user_student
                    messages.success(
                        request, f' { l_firstname_student}  {l_lastname_student} ')
                    obj = login.save(commit=False)
                    obj.person_firstname = l_firstname_student
                    obj.person_lastname = l_lastname_student
                    obj.status = l_status_student
                    obj.save()

                    request.session['pk'] = user_id_student
                    request.session['counsellor'] = l_lastname

                    return redirect('counsellingUrls:indexPage', user_id_student)

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
    students = Students.objects.all()

    request.session['pk'] = pk

    return render(request, 'app/super.html', {
        'objects': objects,
        'pk': pk,
        'count': count,
        'bookings': bookings,
        'meetings': meetings,
        'bookcount': bookcount,
        'meetingcount': meetingcount,
        'students': students,
    })


def adminPage(request, pk):
    objects = Counsellor.objects.all()
    count = Counsellor.objects.all().count()
    bookcount = Bookings.objects.filter(counsellor_user_id=pk).count()
    meetingcount = Meetings.objects.filter(counsellor_user_id=pk).count()
    bookings = Bookings.objects.all().count()
    meetings = Meetings.objects.all().count()
    students = Students.objects.all()

    request.session['pk'] = pk

    return render(request, 'app/admin.html', {
        'objects': objects,
        'students': students,
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
    availiable = AchievementForm()
    day = "Please choose a day from the menu"

    return render(request, 'app/availiable.html', {
        'pk': pk,
        'range': range(8),
        'rang': range(10),
        'availiable': availiable,
        'day': day,

    })


def days(request, pk, day):
    day = day
    availiable = AvailabilityForm()
    pk = request.session['pk']
    counsellor_inst = Counsellor.objects.get(
        user_id=pk)

    if request.method == "POST":
        availiable = AvailabilityForm(request.POST)
        if availiable.is_valid():
            avails = availiable.save(commit=False)
            avails.day = day
            avails.user_id = pk
            avails.counsellor = counsellor_inst
            avails.save()
    return render(request, 'app/availiable.html', {
        'day': day,
        'availiable': availiable,
        'pk': pk,


    })


def times(request, pk, day):
    hours = request.POST.get('hours')
    slots = request.POST.get('slots')
    minutes = request.POST.get('minutes')
    availiable = AvailabilityForm()
    pk = request.session['pk']
    if request.method == 'POST':
        availiable = AvailabilityForm(request.POST)
        if availiable.is_valid():
            time = "time"

    return render(request, 'app/availiable.html', {'time': time,
                                                   'pk': pk,
                                                   'day': day,
                                                   'availiable': availiable,
                                                   })


def homePage(request, pk):

    students = Students.objects.all()
    request.session['pk'] = pk
    return render(request, 'app/home.html', {
        'students': students,
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
    students = Students.objects.all()

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
    # ach_id = request.session['ach_id']
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

                    # ach_obj.id = ach_id
                    ach_obj.save()
                    messages.success(request, f'hi')
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
                                                  'students': students,

                                                  }

                  )


def settingsPage(request, pk):
    objects = Counsellor.objects.all()
    request.session['pk'] = pk
    studentbooks = Bookings.objects.all()
    students = Students.objects.all()

    return render(request, 'app/settings.html', {
        'objects': objects,
        'pk': pk,
        'studentbooks': studentbooks,
        'students': students,

    }

    )


def indexPage(request, pk):
    objects = Counsellor.objects.all()
    request.session['pk'] = pk
    students = Students.objects.all()

    return render(request, 'app/index.html', {
        'objects': objects,
        'students': students,
        'pk': pk,
    })


def popupPage(request, object_user_id):
    objects = Counsellor.objects.all()
    pk = request.session['pk']
    user_id = object_user_id
    students = Students.objects.all()

    return render(request, 'app/popup.html', {
        'objects': objects,
        'pk': pk,
        'user_id': user_id,
        'students': students,
    })


def notificationPage(request, pk):
    objects = Counsellor.objects.all()
    request.session['pk'] = pk
    students = Students.objects.all()
    notification = Notifications.objects.all().order_by('-id')

    return render(request, 'app/notification.html', {
        'objects': objects,
        'pk': pk,
        'students': students,
        'notification': notification,
    })


def profilePage(request, pk):
    objects = Counsellor.objects.all()
    obj_ach = Achievement.objects.all()
    obj_avai = Availability.objects.all()
    obj_exp = Experience.objects.all()
    obj_the = Therapy.objects.all()
    obj_spe = Specialities.objects.all()
    request.session['pk'] = pk
    students = Students.objects.all()

    return render(request, 'app/profile.html', {
        'students': students,
        'objects': objects,
        'pk': pk,
        'obj_ach': obj_ach,
        'obj_avai': obj_avai,
        'obj_exp': obj_exp,
        'obj_the': obj_the,
        'obj_spe': obj_spe,

    })


def student_detail(request, studentbook_student_id):
    students = Students.objects.all()
    objects = Counsellor.objects.all()
    ob = CounsellorForm()
    pk = request.session['pk']
    notifications = NotificationsForm()
    studentbook_student_id = studentbook_student_id

    if request.method == 'POST':
        notifications = NotificationsForm(request.POST)
        ob = CounsellorForm(request.POST)

        if notifications.is_valid():
            for object in objects:
                c_title = object.title
                c_user_id = object.user_id
                c_firstName = object.firstName
                c_lastName = object.lastName
                c_profile = object.profile
                c_email = object.email

                if str(c_user_id) == str(pk):
                    notify = notifications.save(commit=True)
                    notify.counsellor_id = pk
                    notify. counsellor_firstName = c_firstName
                    notify.counsellor_lastName = c_lastName
                    notify.student_id = studentbook_student_id
                    notify.counsellor_title = c_title
                    notify.counsellor_profile = c_profile
                    notify.save()

                    subject = notifications.cleaned_data['subject']
                    text = notifications.cleaned_data['text']

                    for stud in students:
                        s_mail = stud.email
                        s_id = stud.student_id

                        if str(s_id) == str(studentbook_student_id):
                            pass

        else:
            pass
    else:
        notifications = NotificationsForm()

    return render(request, 'app/student.html', {
        'students': students,
        'objects': objects,
        'pk': pk,
        'notifications': notifications,
        'studentbook_student_id': studentbook_student_id,
    })


def search(request, pk):
    pk = request.session['pk']
    students = Students.objects.all()

    search = ''

    if request.method == 'GET':
        search = request.GET.get('search')
        post = Counsellor.objects.all()
        objects = Counsellor.objects.all()
        if search:
            search = request.GET.get('search').split(' ')
            for u in range(len(search)):
                l_search = search[u]

                post = Counsellor.objects.filter(
                    Q(firstName__icontains=l_search) | Q(lastName__icontains=l_search) | Q(title__icontains=l_search))

        else:
            search = ''
        pk = request.session['pk']
        return render(request, 'app/result.html', {
            'post': post,
            'search': search,
            'pk': pk,
            'objects': objects,
            'students': students,

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

    achievements = Achievement.objects.all()

    achieve = Achievement.objects.filter(id=ach_id)
    if achieve.exists():
        try:
            ach_id = int(ach_id)
            ach_id = ach_id + 1
            Achievement.objects.create(id=ach_id)
            request.session['ach_id'] = ach_id

        except:
            pass

    else:
        pass
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
