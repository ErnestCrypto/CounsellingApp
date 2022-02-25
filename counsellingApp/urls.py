# creating urls
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'counsellingUrls'

urlpatterns = [
    path('', views.loginPage, name="loginPage"),
    path('search/<str:pk>/', views.search, name="search"),
    path('admindashboard/<str:pk>/', views.superadminPage, name="superadminPage"),
    path('dashboard/<str:pk>/', views.adminPage, name="adminPage"),
    path('edit/<str:pk>/', views.dashboardPage, name="dashboardPage"),
    path('settings/<str:pk>/', views.settingsPage, name="settingsPage"),
    path('notifications/<str:pk>/',
         views.notificationPage, name="notificationPage"),
    path('index/<str:pk>/',
         views.indexPage, name="indexPage"),
    path('popup/<str:object_user_id>/',
         views.popupPage, name="popupPage"),
    path('profile/<str:pk>/', views.profilePage, name="profilePage"),
    path('delete/<str:studentbook_id>/', views.delete, name="delete"),
    path('update/<str:studentbook_id>/<str:studentbook_status>/',
         views.update, name="update"),
    path('availability_del/<str:av_id>/',
         views.availability_del, name="availability_del"),
    path('availability_add/<str:av_id>/',
         views.availability_add, name="availability_add"),
    path('education_del/<str:ed_id>/',
         views.education_del, name="education_del"),
    path('education_add/<str:ed_id>/',
         views.education_add, name="education_add"),
    path('experience_del/<str:exp_id>/',
         views.experience_del, name="experience_del"),
    path('experience_add/<str:exp_id>/',
         views.experience_add, name="experience_add"),
    path('achievement_del/<str:ach_id>/',
         views.achievement_del, name="achievement_del"),
    path('achievement_add/<str:ach_id>/',
         views.achievement_add, name="achievement_add"),
    path('therapy_del/<str:the_id>/',
         views.therapy_del, name="therapy_del"),
    path('therapy_add/<str:the_id>/',
         views.therapy_add, name="therapy_add"),
    path('speciality_del/<str:spe_id>/',
         views.speciality_del, name="speciality_del"),
    path('availability_add/<str:av_id>/',
         views.speciality_add, name="speciality_add"),
    path('serializers/counsellors/', views.Counsellor_list, name='counsellor_list'),
    path('serializers/counsellors/<int:pk>',
         views.Counsellor_details, name='counsellor_details'),



]

urlpatterns += staticfiles_urlpatterns()

urlpatterns = format_suffix_patterns(urlpatterns)
