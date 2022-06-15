# creating views
from django.shortcuts import render, redirect
from .models import Counsellor, SuperCounsellor, Achievement, Availability, Education, Experience, Therapy, Specialities, Login, Bookings, Meetings, Students, Notifications, SLOTS, MINUTES
from .forms import CounsellorForm, SuperCounsellorForm, AchievementForm, AvailabilityForm, EducationForm, ExperienceForm, TherapyForm, SpecialitiesForm, LoginForm, BookingsForm, NotificationsForm
from django.contrib import messages
import math


def loginPage(request):
    login = LoginForm()
    home = 'red'

    if request.method == "POST":
        login = LoginForm(request.POST)
        person_id = request.POST.get('person_id')
        pin_log = request.POST.get('pin_log')

        user = Counsellor.objects.all()
        student = Students.objects.all()

        if login.is_valid():
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

                    obj = login.save(commit=False)
                    obj.person_firstname = l_firstname
                    obj.person_lastname = l_lastname
                    obj.option = l_status
                    obj.save()

                    request.session['pk'] = user_id
                    request.session['counsellor'] = l_lastname
                    profile = 'red'
                    return redirect('counsellingUrls:dashboardPage', user_id, profile)

            for u in range(len(arr_user_id_student)):

                l_firstname_student = arr_firstname_student[u]
                l_lastname_student = arr_lastname_student[u]
                l_user_student = arr_user_id_student[u]
                l_pin_student = arr_pin_student[u]
                l_status_student = arr_status_student[u]

                if str(l_user_student) == str(person_id) and str(l_pin_student) == str(pin_log):
                    user_id_student = l_user_student

                    obj = login.save(commit=False)
                    obj.person_firstname = l_firstname_student
                    obj.person_lastname = l_lastname_student
                    obj.status = l_status_student
                    obj.save()

                    request.session['pk'] = user_id_student
                    request.session['counsellor'] = l_lastname
                    pk = request.session['pk']
                    return redirect('bookingUrls:indexPage', pk)

    return render(request, 'app/login.html', {
        'log': login

    })


def superadminPage(request, pk, admin):
    objects = Counsellor.objects.all()
    count = Counsellor.objects.all().count()
    bookcount = Bookings.objects.filter(counsellor_user_id=pk).count()
    meetingcount = Meetings.objects.filter(counsellor_user_id=pk).count()
    bookings = Bookings.objects.all().count()
    books = Bookings.objects.all()
    meetings = Meetings.objects.all().count()
    students = Students.objects.all()

    request.session['pk'] = pk
    admin = 'red'
    return render(request, 'app/super.html', {
        'objects': objects,
        'pk': pk,
        'books': books,
        'admin': admin,
        'count': count,
        'bookings': bookings,
        'meetings': meetings,
        'bookcount': bookcount,
        'meetingcount': meetingcount,
        'students': students,
    })


def list(request, pk):
    admin = 'red'
    count = Counsellor.objects.all().count()
    objects = Counsellor.objects.all()
    return render(request, 'app/list.html', {
        'objects': objects,
        'pk': pk,
        'admin': admin,
        'count': count,

    })


def del_counsellor(request, object_id):
    pk = request.session['pk']
    counsellor = Counsellor.objects.get(id=object_id)
    counsellor.delete()
    return redirect('counsellingUrls:list', pk)


def counsellor_list(request, pk):
    dashboard = 'red'
    count = Counsellor.objects.all().count()
    objects = Counsellor.objects.all()
    return render(request, 'app/counsellors.html', {
        'objects': objects,
        'pk': pk,
        'dashboard': dashboard,
        'count': count,
    })


def addcounsellor(request, pk):
    red = 'red'
    admin = 'app/admin.html'
    profile = 'app/profile.html'
    notification = 'app/notification.html'
    index = 'app/index.html'
    counsellor = CounsellorForm()
    objects = Counsellor.objects.all()
    request.session['pk'] = pk

    if request.method == 'POST':

        counsellor = CounsellorForm(request.POST, request.FILES)

        if counsellor.is_valid():
            counsellor.save()

        else:
            counsellor = CounsellorForm()

    return render(request, 'app/add.html', {'profile': profile,
                                            'notification': notification,
                                            'index': index,
                                            'admin': admin,
                                            'counsellor':  counsellor,

                                            'Counsellor': counsellor,
                                            'objects': objects,
                                            'pk': pk,


                                            'admin': red,
                                            }

                  )


def adminPage(request, pk, dashboard):
    objects = Counsellor.objects.all()
    count = Counsellor.objects.all().count()
    bookcount = Bookings.objects.filter(counsellor_user_id=pk).count()
    meetingcount = Meetings.objects.filter(counsellor_user_id=pk).count()
    bookings = Bookings.objects.all().count()
    meetings = Meetings.objects.all().count()
    students = Students.objects.all()
    dashboard = 'red'
    request.session['pk'] = pk
    counselor = Counsellor.objects.get(user_id=pk)
    myTimes = Availability.objects.filter(counsellor=counselor)

    return render(request, 'app/admin.html', {
        'objects': objects,
        'students': students,
        'pk': pk,
        'dashboard': dashboard,
        'count': count,
        'bookings': bookings,
        'meetings': meetings,
        'bookcount': bookcount,
        'meetingcount': meetingcount,
        'myTimes': myTimes,
    })


def availiablePage(request, pk):
    pk = request.session['pk']
    availiable = AvailabilityForm()
    day = "MONDAY"
    instruction = 2
    return render(request, 'app/availiable.html', {
        'pk': pk,
        'range': range(8),
        'rang': range(10),
        'availiable': availiable,
        'day': day,
        'instruction': instruction,
        'm_option': MINUTES,
        's_option': SLOTS,

    })


def days(request, pk, day):
    availiable = AvailabilityForm()
    pk = request.session['pk']
    request.session['day'] = day
    counsellor_inst = Counsellor.objects.get(
        user_id=pk)
    instruction = 2

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
        'instruction': instruction,
        'm_option': MINUTES,
        's_option': SLOTS,


    })


def times(request, pk, day):
    if request.method == 'POST':
        hours = int(request.POST.get('hours'))
        slots = int(request.POST.get('slots'))
        minutes = int(request.POST.get('minutes'))
        checked = "white"

    else:
        hours = request.session['hours']
        minutes = request.session['minutes']
        slots = request.session['slots']
        checked = request.session['checked']

    request.session['day'] = day

    availiable = AvailabilityForm()
    pk = request.session['pk']
    request.session['hours'] = hours
    request.session['minutes'] = minutes
    request.session['slots'] = slots

    if request.method == 'POST' or request.method == 'GET':
        availiable = AvailabilityForm(request.POST)
        if availiable.is_valid():
            start = 28800  # time in seconds for 8:00 am
            end = 68400  # time in seconds for 7:00 pm

            interval = end - start
            hours_sec = hours*3600
            minutes_sec = minutes * 60
            chosen_time = hours_sec + minutes_sec
            if chosen_time == 0:
                final = 0
            else:
                final = interval/chosen_time
            if (hours == 0):
                final_floor = int(math.ceil(final))
            elif (hours == 1):
                final_floor = int(math.ceil(final))
            elif(hours == 2):
                final_floor = int(math.floor(final))
            elif(hours == 3):
                final_floor = int(math.floor(final))
            elif(hours == 4):
                final_floor = int(math.floor(final))
            elif(hours == 5):
                final_floor = int(math.floor(final))
            ran = range(final_floor)
            d_ran = final_floor * 2
            d_ran = range(d_ran)
            break_time = 600
            t_time = chosen_time - break_time

            time = []

            for i in d_ran:
                if start < end:
                    time_in_hours = start/3600
                    h, d = divmod(time_in_hours, 1)

                    f_start = int(h)
                    if f_start < 10:
                        f_start = str(f_start)
                        f_start = "0" + f_start

                    if int(f_start) > 12:
                        f_start = f_start - 12

                    time_in_minutes = int(d*60)
                    s, m = divmod(time_in_minutes, 1)
                    m_start = int(s)
                    if m_start < 10:
                        m_start = "0" + str(m_start)
                    started = str(f_start) + \
                        ":" + str(m_start)
                    time.append(started)

                start = start + chosen_time

            e_time = time[1:]
            add = time + e_time
            add.sort()
            lim = len(add)
            lim = int(lim)

            if (lim % 2) == 0:
                my = add
            else:
                mine = add.append('7:00')

            subTime = [add[n:n+2] for n in range(0, len(add), 2)]
            request.session['subTime'] = subTime

    return render(request, 'app/availiable.html', {
        'pk': pk,
        'day': day,
        'ran': ran,
        'availiable': availiable,
        'time': subTime,
        'm_option': MINUTES,
        's_option': SLOTS,
        'checked': checked,

    })


def schedule(request, pk, day):
    if request.method == 'POST':
        start = request.POST.getlist('start_time')
        end = request.POST.getlist('end_time')
        box = request.POST.getlist('checkbox')
        hours = request.session['hours']
        minutes = request.session['minutes']
        slots = request.session['slots']
        request.session['day'] = day
        availiable = AvailabilityForm(request.POST)
        user = Counsellor.objects.get(user_id=pk)
        already = Availability.objects.filter(counsellor=user, day=day).first()

        if already:
            availiable = AvailabilityForm(request.POST, instance=already)
            if availiable.is_valid():
                myTime = availiable.save(commit=False)
                if hours or minutes:
                    myTime.availabletime = box
                    myTime.startime = start
                    myTime.endtime = end
                    myTime.slots = slots
                    myTime.counsellor = user
                    myTime.user_id = pk
                    myTime.hours = hours
                    myTime.minutes = minutes
                    myTime.day = day
                    myTime.save()
                    instruction = 1

            else:
                instruction = 3

        else:
            availiable = AvailabilityForm(request.POST)
            if availiable.is_valid():
                myTime = availiable.save(commit=False)
                if hours or minutes:
                    myTime.availabletime = box
                    myTime.startime = start
                    myTime.endtime = end
                    myTime.counsellor = user
                    myTime.user_id = pk
                    myTime.hours = hours
                    myTime.slots = slots
                    myTime.minutes = minutes
                    myTime.day = day
                    myTime.save()
                    instruction = 1

            else:
                instruction = 3

        day = request.session['day']

    return render(request, 'app/availiable.html', {
        'day': day,
        'pk': pk,
        'availiable': availiable,
        'instruction': instruction,
        'm_option': MINUTES,
        's_option': SLOTS,
    })


def add_period(request, n, u, counter):
    day = request.session['day']
    pk = request.session['pk']
    request.session['checked'] = 'lightgreen'
    request.session['counter'] = counter
    counsellor = Counsellor.objects.get(user_id=pk)
    if request.method == 'POST':
        availiable = Availability.save(commit=False)

    return redirect('counsellingUrls:times', pk, day)


def del_period(request, n, u, counter):
    day = request.session['day']
    pk = request.session['pk']
    request.session['checked'] = 'white'
    request.session['counter'] = counter
    return redirect('counsellingUrls:times', pk, day)


def homePage(request, pk):

    students = Students.objects.all()
    request.session['pk'] = pk
    return render(request, 'app/home.html', {
        'students': students,
        'pk': pk,

    }

    )


def dashboardPage(request, pk, profile):
    profile = 'red'
    notification = 'app/notification.html'
    counsellor = CounsellorForm()
    objects = Counsellor.objects.all()
    students = Students.objects.all()
    count = Counsellor.objects.all().count()
    request.session['pk'] = pk

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
        coun = Counsellor.objects.get(user_id=pk)
        counsellor = CounsellorForm(request.POST, request.FILES, instance=coun)
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
                    counsellor_inst = Counsellor.objects.get(
                        id=l_counsellor_id)

        else:
            counsellor = CounsellorForm()

    return render(request, 'app/dashboard.html', {'profile': profile,
                                                  'notification': notification,
                                                  'counsellor':  counsellor,
                                                  'Counsellor': counsellor,
                                                  'objects': objects,
                                                  'pk': pk,
                                                  'count': count,
                                                  'students': students,

                                                  }

                  )


def settingsPage(request, pk, settings):
    objects = Counsellor.objects.all()
    request.session['pk'] = pk
    studentbooks = Bookings.objects.all()
    students = Students.objects.all()
    settings = 'red'
    return render(request, 'app/settings.html', {
        'objects': objects,
        'pk': pk,
        'studentbooks': studentbooks,
        'students': students,
        'settings': settings,

    }

    )


def notificationPage(request, pk, notify):
    objects = Counsellor.objects.all()
    request.session['pk'] = pk
    students = Students.objects.all()
    notification = Notifications.objects.all().order_by('-id')
    notify = 'red'
    return render(request, 'app/notification.html', {
        'objects': objects,
        'pk': pk,
        'notify': notify,
        'students': students,
        'notification': notification,
    })


def student_detail(request, studentbook_student_id):
    students = Students.objects.all()
    objects = Counsellor.objects.all()
    ob = CounsellorForm()
    pk = request.session['pk']
    notifications = NotificationsForm()
    studentbook_student_id = studentbook_student_id
    settings = 'red'
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
        'settings': settings,
        'pk': pk,
        'notifications': notifications,
        'studentbook_student_id': studentbook_student_id,
    })


def delete(request, studentbook_id):
    pk = request.session['pk']
    book = Bookings.objects.get(id=studentbook_id)
    book.delete()
    return redirect('counsellingUrls:settingsPage', pk)


def update(request, studentbook_id, studentbook_status):
    pk = request.session['pk']

    book_id = Bookings.objects.get(id=studentbook_id)
    bookings = Bookings.objects.all()
    books = BookingsForm(instance=book_id)
    settings = 'red'
    for booking in bookings:
        if int(booking.id) == int(studentbook_id):
            if str(studentbook_status) == 'Pending':
                booksave = books.save(commit=False)
                booksave.student_status = 'Approved'
                booksave.save()

            elif str(studentbook_status) == 'Approved':
                booksave = books.save(commit=False)
                booksave.student_status = 'Pending'
            booksave.save()

    return redirect('counsellingUrls:settingsPage', pk, settings)


def mytimes(request, pk):
    pk = request.session['pk']
    availabiles = Availability.objects.all()

    return render(request, 'app/time.html', {
        'pk': pk,
        'availabiles': availabiles

    })


def deletetime(request, availabile_id):
    pk = request.session['pk']
    availabile = Availability.objects.get(id=availabile_id)
    availabile.delete()
    return redirect('counsellingUrls:mytimes', pk)


def website(request):
    pk = request.session['pk']
    return redirect('bookingUrls:indexPage', pk)


def clear(request, pk):
    profile = 'red'
    counsellor = Counsellor.objects.filter(user_id=pk).first()

    try:
        counsellor_profile = counsellor.profile
        counsellor_profile.delete()
    except:
        pass
    return redirect('counsellingUrls:dashboardPage', pk, profile)
