# Registering our models
from django.contrib import admin
from django import forms
from .models import Counsellor,  SuperCounsellor, Achievement, Availability, Education, Experience, Therapy, Specialities, Login, Bookings, Meetings, Notifications, Students
import datetime
import calendar
from django.urls import reverse
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe


class TherapyInline(admin.StackedInline):
    model = Therapy


class SpecialitiesInline(admin.StackedInline):
    model = Specialities


class AchievemenetsInline(admin.StackedInline):
    model = Achievement


class AvailabilityInline(admin.StackedInline):
    model = Availability


class EducationInline(admin.StackedInline):
    model = Education


class ExperienceInline(admin.StackedInline):
    model = Experience


@admin.register(Therapy)
class TherapyAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'therapies_offered', 'user_id', 'counsellor',
    ]


@admin.register(Specialities)
class SpecialitiesAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'top_specialities', 'user_id', 'counsellor',
    ]


@admin.register(Education)
class EductaionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'education_institution',
        'year_completed', 'user_id', 'counsellor',
    ]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'experience_institution',
        'experience_position', 'user_id',  'counsellor',
    ]


@admin.register(Achievement)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'awards', 'user_id', 'counsellor', ]


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ['id', 'day', 'start_time', 'end_time', 'notes',
                    'user_id', 'counsellor', ]


@admin.register(Counsellor)
class CounsellorAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'profile', 'user_id', 'pin', 'status', 'title', 'firstName', 'lastName', 'occupation',
        'email', 'contact',
        'gender',
    ]

    inlines = [
        AchievemenetsInline,
        AvailabilityInline,
        EducationInline,
        ExperienceInline,
        TherapyInline,
        SpecialitiesInline,
    ]


@admin.register(SuperCounsellor)
class SuperCounsellorAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'profile', 'user_id', 'pin', 'status', 'title', 'firstName', 'occupation',
        'lastName', 'gender', 'email', 'contact',
    ]


@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = [
        'person_firstname',
        'person_lastname',
        'person_id',
        'pin_log',
        'option',
        'date'
    ]


@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'counsellor',
        'counsellor_user_id',
        'student_id',
        'student_name',
        'student_profile',
        'date',

        'student_status',
    ]


@admin.register(Meetings)
class MeetingsAdmin(admin.ModelAdmin):
    list_display = [

        'counsellor',
        'counsellor_user_id',
        'student_id',
        'student_name',
        'student_profile',
        'date',

    ]


@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = [
        'counsellor_id',
        'counsellor_title',
        'counsellor_firstName',
        'counsellor_lastName',
        'student_id',
        'date',
        'time',
        'text',
    ]


@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'student_id',
        'pin',
        'profile',
        'firstName',
        'lastName',
        'age',
        'contact',
        'status',
    ]
