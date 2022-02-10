# Creating the models
from email.policy import default
from django.db import models


TITLE = [
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Dr.', 'Dr.'),
    ('Prof.', 'Prof.'),
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
    ('admin', 'Admin'),
    ('counsellor', 'Counsellor'),
    ('student', 'Student'),
    ('staff', 'Staff'),
]


class BaseModel(models.Model):
    title = models.CharField(choices=TITLE, default=None,
                             max_length=20, db_index=True, null=True, blank=True)
    firstName = models.CharField(
        max_length=255, db_index=True, blank=True, default=None, null=True,)
    lastName = models.CharField(
        max_length=255, db_index=True, blank=True, default=None, null=True, )
    occupation = models.CharField(
        max_length=255, db_index=True, blank=True, null=True, default=None, )
    gender = models.CharField(choices=GENDER,
                              default=None, max_length=25, db_index=True, null=True, blank=True)
    email = models.EmailField(default=None, blank=True, null=True,)
    contact = models.IntegerField(default=None,  blank=True, null=True, )
    profile = models.ImageField(
        upload_to='images/', default=None, null=True, blank=True,)
    pin = models.IntegerField(default=None, null=True,
                              blank=True, )
    user_id = models.IntegerField(
        default=None, null=True, blank=True, )
    status = models.CharField(
        max_length=255, choices=LOGIN, default=None, null=True, blank=True, )

    class Meta:
        abstract = True

    def __str__(self):
        return self.lastName


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
    start_time = models.TimeField(default=None,  null=True, blank=True)
    end_time = models.TimeField(default=None,  null=True, blank=True)
    date = models.CharField(choices=DAYS, default=None,
                            null=True, max_length=255, blank=True)
    user_id = models.CharField(
        max_length=255, db_index=True, blank=True, null=True, default=None)

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
