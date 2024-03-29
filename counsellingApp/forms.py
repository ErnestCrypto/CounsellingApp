# Creating our form models
from django import forms
from django.forms import ModelForm
from .models import Counsellor, SuperCounsellor, Achievement, Availability, Education, Experience, Therapy, Specialities, Login, Bookings, Notifications, Students


class SpecialitiesForm(ModelForm):
    class Meta:
        model = Specialities
        exclude = ['counsellor', ]
        fields = "__all__"
        widgets = {
            'top_specialities': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TherapyForm(ModelForm):
    class Meta:
        model = Therapy
        exclude = ['counsellor', ]
        fields = "__all__"
        widgets = {
            'therapies_offered': forms.TextInput(attrs={'class': 'form-control'}),

        }


class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ['counsellor', ]
        fields = "__all__"
        widgets = {
            'education_institution': forms.TextInput(attrs={'class': 'form-control'}),
            'year_completed': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AchievementForm(ModelForm):
    class Meta:
        model = Achievement
        exclude = ['counsellor', ]
        fields = "__all__"
        widgets = {
            'awards': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ['counsellor', ]
        fields = "__all__"
        widgets = {
            'experience_institution': forms.TextInput(attrs={'class': 'form-control'}),
            'experience_position': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AvailabilityForm(ModelForm):
    class Meta:
        model = Availability
        fields = "__all__"
        widgets = {
            'breaks': forms.Select(attrs={'class': 'form-control', 'id': 'focusid', }),
            'minutes': forms.Select(attrs={'class': 'form-control', 'id': 'focusid', }),
            'hours': forms.Select(attrs={'class': 'form-control', 'id': 'focusid', }),
            'slots': forms.Select(attrs={'class': 'form-control', 'id': 'focusid', }),
            'day': forms.TextInput(attrs={'class': 'form-control',  'type': 'text'}),
            'startime': forms.TextInput(attrs={'class': 'form-control',  'type': 'text'}),
            'endtime': forms.TextInput(attrs={'class': 'form-control',  'type': 'text'}),
            'not_availiable': forms.CheckboxInput(attrs={}),


        }


class CounsellorForm(ModelForm):

    class Meta:
        model = Counsellor

        fields = "__all__"
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control', 'id': 'focusid', }),
            'status': forms.Select(attrs={'class': 'form-control', 'id': 'focusid', }),
            'firstName': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'user_id': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'id': 'focusid'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
            'profile': forms.ClearableFileInput(attrs={'class': 'image_profile', 'type': 'file'}),

        }


class SuperCounsellorForm(ModelForm):
    class Meta:
        model = SuperCounsellor
        fields = "__all__"
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'user_id': forms.TextInput(attrs={'class': 'form-control', 'readOnly': 'false'}),
            'profile': forms.ClearableFileInput(attrs={'class': 'image_profile', 'type': 'file'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),


        }


class LoginForm(ModelForm):

    class Meta:
        model = Login
        fields = "__all__"
        widgets = {
            'person_id': forms.TextInput(attrs={'placeholder': 'ID', 'class': 'fadeIn second', 'type': 'text'}),
            'pin_log': forms.TextInput(attrs={'placeholder': 'PIN', 'class': 'fadeIn third', 'type': 'password'}),
            'option': forms.Select(attrs={'class': 'fadeIn fourth', 'type': 'select'}),
        }


class BookingsForm(ModelForm):
    class Meta:
        model = Bookings
        fields = "__all__"


class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
        widget = {
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'profile': forms.ClearableFileInput(attrs={'class': 'image_profile', 'type': 'file'}),

        }


class NotificationsForm(ModelForm):
    class Meta:
        model = Notifications
        fields = "__all__"
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'counsellor_id ': forms.TextInput(attrs={'class': 'form-control'}),
            'counsellor_title': forms.TextInput(attrs={'class': 'form-control'}),
            'counsellor_firstName': forms.TextInput(attrs={'class': 'form-control'}),
            'counsellor_lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.TextInput(attrs={'class': 'form-control'}),
        }
