# creating urls
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'counsellingUrls'

urlpatterns = [
    path('', views.loginPage, name="loginPage"),
    path('search/<slug:pk>/', views.search, name="search"),
    path('admindashboard/<slug:pk>/', views.superadminPage, name="superadminPage"),
    path('dashboard/<slug:pk>/', views.adminPage, name="adminPage"),
    path('edit/<slug:pk>/', views.dashboardPage, name="dashboardPage"),
    path('settings/<slug:pk>/', views.settingsPage, name="settingsPage"),
    path('notifications/<slug:pk>/',
         views.notificationPage, name="notificationPage"),
    path('index/<slug:pk>/',
         views.indexPage, name="indexPage"),
    path('popup/<slug:object_user_id>/',
         views.popupPage, name="popupPage"),
    path('profile/<slug:pk>/', views.profilePage, name="profilePage"),
    path('delete/<slug:studentbook_id>/', views.delete, name="delete"),
    path('update/<slug:studentbook_id>/<slug:studentbook_status>/',
         views.update, name="update"),
    path('availability_del/<slug:av_id>/',
         views.availability_del, name="availability_del"),
    path('availability_add/<slug:av_id>/',
         views.availability_add, name="availability_add"),
    path('education_del/<slug:ed_id>/',
         views.education_del, name="education_del"),
    path('education_add/<slug:ed_id>/',
         views.education_add, name="education_add"),
    path('experience_del/<slug:exp_id>/',
         views.experience_del, name="experience_del"),
    path('experience_add/<slug:exp_id>/',
         views.experience_add, name="experience_add"),
    path('achievement_del/<slug:ach_id>/',
         views.achievement_del, name="achievement_del"),
    path('achievement_add/<slug:ach_id>/',
         views.achievement_add, name="achievement_add"),
    path('therapy_del/<slug:the_id>/',
         views.therapy_del, name="therapy_del"),
    path('therapy_add/<slug:the_id>/',
         views.therapy_add, name="therapy_add"),
    path('speciality_del/<slug:spe_id>/',
         views.speciality_del, name="speciality_del"),
    path('availability_add/<slug:av_id>/',
         views.speciality_add, name="speciality_add"),
    path('serializers/counsellors/', views.Counsellor_list, name='counsellor_list'),
    path('serializers/counsellors/<slug:pk>/',
         views.Counsellor_details, name='counsellor_details'),
    path('availiability/<slug:pk>/',
         views.availiablePage, name='availiablePage'),
    path('calendar/', views.calender, name='calender'),
    path('test/', views.test, name='test')


]

urlpatterns += staticfiles_urlpatterns()

urlpatterns = format_suffix_patterns(urlpatterns)
