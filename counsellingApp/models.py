# Creating the models
from email.policy import default
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
import uuid
from django.contrib.postgres.fields import ArrayField
TITLE = [
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Dr.', 'Dr.'),
    ('Prof.', 'Prof.'),
    ('Rev.Dr.', 'Rev.Dr.'),
    ('Dr.Mr.', 'Dr.Mr.'),
    ('Dr.Mrs.', 'Dr.Mrs.'),
    ('Rev.Fr.', 'Rev.Fr.'),
    ('Rev.Fr.Dr.', 'Rev.Fr.Dr.'),
]

GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
]

DAYS = [
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wednesday', 'Wednesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
]
LOGIN = [
    ('ADMIN', 'Admin'),
    ('COUNSELLOR', 'Counsellor'),
    ('STUDENT', 'Student'),

]

BOOKING = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
]

SLOTS = [
    ('0', '00'),
    ('1', '01'),
    ('2', '02'),
    ('3', '03'),
    ('4', '04'),
    ('5', '05'),


]

MINUTES = [
    ('0', '00'),
    ('5', '05'),
    ('10', '10'),
    ('15', '15'),
    ('20', '20'),
    ('25', '25'),
    ('30', '30'),
    ('35', '35'),
    ('40', '40'),
    ('45', '45'),
    ('50', '50'),
    ('55', '55'),
]


class BaseModel(models.Model):
    title = models.CharField(choices=TITLE, default=None,
                             max_length=20, db_index=True, null=True, blank=True)
    firstName = models.CharField(
        max_length=255, db_index=True, default=None, null=True, blank=True)
    lastName = models.CharField(
        max_length=255, db_index=True,  default=None, null=True, blank=True)
    occupation = models.CharField(
        max_length=255, db_index=True,  default=None, null=True, blank=True)
    gender = models.CharField(choices=GENDER,
                              default=None, max_length=25, db_index=True, null=True, blank=True)
    email = models.EmailField(default=None, null=True, blank=True)
    contact = models.IntegerField(default=None, null=True, blank=True)
    profile = models.ImageField(
        upload_to='images/', default=None, null=True, blank=True)
    pin = models.IntegerField(default=None, null=True, blank=True)
    user_id = models.IntegerField(
        default=None, null=True, blank=True)
    status = models.CharField(
        max_length=255, choices=LOGIN, default='COUNSELLOR', null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.lastName + ' ' + self.firstName


class SuperCounsellor(BaseModel):

    class Meta:
        verbose_name_plural = 'Super Counsellors'


class Counsellor(BaseModel):
    about = models.TextField(blank=True, default=None, null=True)


class Education(models.Model):
    counsellor = models.ForeignKey(
        Counsellor, related_name="education", on_delete=models.CASCADE, default=None, blank=True, null=True)
    education_institution = models.CharField(
        max_length=255, db_index=True, blank=True, default=None, null=True)
    year_completed = models.CharField(
        max_length=255, db_index=True, default=None, blank=True, null=True)
    user_id = models.CharField(
        max_length=255, db_index=True, blank=True, null=True, default=None)

    class Meta:
        verbose_name_plural = 'education'


class Achievement(models.Model):
    counsellor = models.ForeignKey(
        Counsellor,  related_name='achievement', on_delete=models.CASCADE, blank=True, default=None, null=True)
    awards = models.CharField(
        max_length=255, db_index=True, blank=True, default=None, null=True)
    user_id = models.CharField(
        max_length=255, db_index=True, blank=True, null=True, default=None)


class Availability(models.Model):
    counsellor = models.ForeignKey(
        Counsellor, related_name='availability', on_delete=models.CASCADE, blank=True, default=None, null=True)
    user_id = models.CharField(
        max_length=255, db_index=True, blank=True, null=True, default=None)
    day = models.CharField(default=None,
                           null=True, max_length=255, blank=True)
    slots = models.CharField(max_length=255,
                             choices=SLOTS, default='0', null=True, blank=True)
    hours = models.CharField(max_length=255,
                             choices=SLOTS, default='0', null=True, blank=True)
    minutes = models.CharField(max_length=255,
                               choices=MINUTES, default='5', null=True, blank=True)
    breaks = models.CharField(max_length=255,
                              choices=MINUTES, default='5', null=True, blank=True)
    startime = models.TextField(
        default=None, null=True, blank=True)
    endtime = models.TextField(
        default=None, null=True, blank=True)
    availabletime = models.TextField(
        default=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = "availabilities"


class Experience(models.Model):
    counsellor = models.ForeignKey(
        Counsellor, related_name="experience", on_delete=models.CASCADE, blank=True, default=None, null=True)
    experience_institution = models.CharField(
        max_length=255, db_index=True, blank=True, default=None, null=True)
    experience_position = models.CharField(
        max_length=255, db_index=True,  blank=True, default=None, null=True)
    user_id = models.CharField(
        max_length=255, db_index=True, blank=True, null=True, default=None)


class Therapy(models.Model):
    counsellor = models.ForeignKey(
        Counsellor, related_name='therapy', on_delete=models.CASCADE, blank=True, default=None, null=True)
    therapies_offered = models.CharField(
        max_length=255, db_index=True, default=None, blank=True, null=True)
    user_id = models.CharField(
        max_length=255, db_index=True, blank=True, null=True, default=None)

    class Meta:
        verbose_name_plural = 'therapies'


class Specialities(models.Model):
    counsellor = models.ForeignKey(
        Counsellor, related_name='specialities', on_delete=models.CASCADE, blank=True, default=None, null=True)
    top_specialities = models.CharField(
        max_length=255, db_index=True, default=None, blank=True, null=True)
    user_id = models.CharField(
        max_length=255, db_index=True, blank=True, null=True, default=None)

    class Meta:
        verbose_name_plural = 'specialities'


class Login(models.Model):
    person_firstname = models.CharField(max_length=255, default=None,
                                        null=True, blank=True, db_index=True)
    person_lastname = models.CharField(max_length=255, default=None,
                                       null=True, blank=True, db_index=True)
    person_id = models.CharField(
        max_length=255, db_index=True, default=None, blank=True, null=True)
    pin_log = models.IntegerField(
        db_index=True, default=None, blank=True, null=True)
    option = models.CharField(
        max_length=255, choices=LOGIN, default=None, blank=True, null=True,)
    date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)


class Bookings(models.Model):
    counsellor = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    counsellor_user_id = models.IntegerField(
        default=None, null=True, blank=True)
    student_id = models.IntegerField(
        default=None, null=True, blank=True)
    student_name = models.CharField(
        max_length=255, db_index=True, default=None, null=True, blank=True)

    student_profile = models.ImageField(
        upload_to='images/', default=None, null=True, blank=True)

    date = models.DateTimeField(
        null=True, max_length=255, blank=True, auto_now_add=True, )

    student_status = models.CharField(choices=BOOKING,
                                      max_length=255, db_index=True, default='Pending', null=True, blank=True)
    time = models.CharField(max_length=255, db_index=True,
                            default=None, null=True, blank=True)
    day = models.CharField(max_length=255, db_index=True,
                           default=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Bookings'


class Meetings(models.Model):
    counsellor = models.ForeignKey(
        Counsellor, related_name='meetings', on_delete=models.CASCADE, default=None, )
    counsellor_user_id = models.IntegerField(
        default=None, null=True, blank=True)
    student_id = models.IntegerField(
        default=None, null=True, blank=True)
    student_name = models.CharField(
        max_length=255, db_index=True, default=None, null=True, blank=True)

    student_profile = models.ImageField(
        upload_to='images/', default=None, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True,
                                null=True, max_length=255, blank=True)

    class Meta:
        verbose_name_plural = 'Meetings'


class Notifications(models.Model):
    counsellor_id = models.CharField(max_length=255, null=True, blank=True)
    counsellor_title = models.CharField(
        max_length=255, default=None, null=True, blank=True)
    counsellor_firstName = models.CharField(
        max_length=255, default=None, null=True, blank=True)
    counsellor_lastName = models.CharField(
        max_length=255, default=None, null=True, blank=True)
    student_id = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(default=None)
    subject = models.CharField(max_length=255, default=None)
    counsellor_profile = models.ImageField(
        upload_to='images/', default=None, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now=True)
    date_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Notifications"


class Students(models.Model):
    student_id = models.IntegerField()
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    age = models.IntegerField(default=None, null=True, blank=True)
    status = models.CharField(
        max_length=255, choices=LOGIN, default='STUDENT')
    profile = models.ImageField(upload_to='images/', blank=True, null=True)
    contact = models.IntegerField(default=None, null=True, blank=True)
    pin = models.IntegerField(default=None, null=True, blank=True)
    email = models.CharField(
        max_length=255, db_index=True, default=None, null=True, blank=True)
    course = models.CharField(
        max_length=255, db_index=True, default=None, null=True, blank=True)
    level = models.CharField(
        max_length=255, db_index=True, default=None, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Students"


"""
KA PMB 36 KIA Accra, Ghana

 Digital Address: GL – 125 – 6946

+233 (0) 302 550 612

"""
