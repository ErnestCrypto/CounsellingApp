# Registering our models
from django.contrib import admin
from django import forms
from .models import Counsellor,  SuperCounsellor, Achievement, Availability, Education, Experience, Therapy, Specialities, Login


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
        'id', 'therapies_offered', 'counsellor',
    ]


@admin.register(Specialities)
class SpecialitiesAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'top_specialities', 'counsellor',
    ]


@admin.register(Education)
class EductaionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'education_institution',
        'year_completed', 'counsellor',
    ]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'experience_institution',
        'experience_position',  'counsellor',
    ]


@admin.register(Achievement)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'awards', 'counsellor', ]


@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'start_time', 'end_time',
                    'counsellor', ]


@admin.register(Counsellor)
class CounsellorAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'firstName', 'lastName', 'email', 'contact',
        'gender', 'about', 'profile'
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
        'id', 'title', 'firstName', 'lastName', 'gender', 'email', 'contact', 'profile'
    ]


@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display = [
        'person',
        'person_id',
        'pin',
        'option',
        'date'
    ]
