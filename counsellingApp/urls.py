# creating urls
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import api_views
app_name = 'counsellingUrls'

urlpatterns = [
    path('', views.loginPage, name="loginPage"),
    path('search/<str:pk>', views.search, name="search"),
    path('schedule/<str:pk>/<str:day>', views.schedule, name="schedule"),
    path('addPeriod/<str:n>/<str:u>', views.add_period, name="add_period"),
    path('delPeriod/<str:n>/<str:u>', views.del_period, name="del_period"),
    path('del/<str:object_id>',
         views.del_counsellor, name="del_counsellor"),
    path('all_counsellors/<str:pk>',
         views.counsellor_list, name="all_counsellors"),

    path('admindashboard/<str:pk>/<str:admin>/',
         views.superadminPage, name="superadminPage"),
    path('list/<str:pk>/',
         views.list, name="list"),
    path('counsellors/<str:pk>/', views.addcounsellor, name="addcounsellor"),
    path('dashboard/<str:pk>/<str:dashboard>/',
         views.adminPage, name="adminPage"),
    path('edit/<str:pk>/', views.dashboardPage, name="dashboardPage"),
    path('settings/<str:pk>/', views.settingsPage, name="settingsPage"),
    path('notifications/<str:pk>/<str:notify>/',
         views.notificationPage, name="notificationPage"),
    path('index/<str:pk>/<str:home>/',
         views.indexPage, name="indexPage"),
    path('popup/<str:object_user_id>/',
         views.popupPage, name="popupPage"),
    path('profile/<str:pk>/<str:profile>/',
         views.profilePage, name="profilePage"),
    path('delete/<str:studentbook_id>/', views.delete, name="delete"),
    path('update/<str:studentbook_id>/<str:studentbook_status>/',
         views.update, name="update"),
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
    path('speciality_add/<str:spe_id>/',
         views.speciality_add, name="speciality_add"),

    path('availiability/<str:pk>/',
         views.availiablePage, name='availiablePage'),
    path('calendar/', views.calender, name='calender'),
    path('test/', views.test, name='test'),
    path('details/<int:studentbook_student_id>',
         views.student_detail, name='student_details'),
    path('availiability/<str:pk>/<str:day>/', views.days, name='days'),
    path('availiability/<str:pk>/<str:day>/times', views.times, name='times'),
    #     path("/dfadf/", views.CounsellorList.as_view(), name="kldjfad")

]


urlpatterns += [
    path('serializers/counsellors/',
         api_views.counsellor_list, name='counsellor_list'),
    path('serializers/counsellors/<str:pk>/',
         api_views.counsellor_details, name='counsellor_details'),

]


urlpatterns += staticfiles_urlpatterns()

urlpatterns = format_suffix_patterns(urlpatterns)
