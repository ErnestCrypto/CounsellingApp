# creating urls
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import api_views
app_name = 'counsellingUrls'

urlpatterns = [
    path('', views.loginPage, name="loginPage"),
    path('ugcounselling/', views.website, name="website"),
    path('schedule/<str:pk>/<str:day>', views.schedule, name="schedule"),
    path('addPeriod/<str:n>/<str:u>/<int:counter>/',
         views.add_period, name="add_period"),
    path('delPeriod/<str:n>/<str:u>/<int:counter>/',
         views.del_period, name="del_period"),
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
    path('edit/<str:pk>/<str:profile>/',
         views.dashboardPage, name="dashboardPage"),
    path('settings/<str:pk>/<str:settings>/',
         views.settingsPage, name="settingsPage"),
    path('notifications/<str:pk>/<str:notify>/',
         views.notificationPage, name="notificationPage"),
    path('delete/<str:studentbook_id>/', views.delete, name="delete"),
    path('update/<str:studentbook_id>/<str:studentbook_status>/',
         views.update, name="update"),
    path('availiability/<str:pk>/',
         views.availiablePage, name='availiablePage'),

    path('details/<int:studentbook_student_id>',
         views.student_detail, name='student_details'),
    path('availiability/<str:pk>/<str:day>/', views.days, name='days'),
    path('availiability/<str:pk>/<str:day>/times', views.times, name='times'),

]


urlpatterns += [
    path('serializers/counsellors/',
         api_views.counsellor_list, name='counsellor_list'),
    path('serializers/counsellors/<str:pk>/',
         api_views.counsellor_details, name='counsellor_details'),

]


urlpatterns += staticfiles_urlpatterns()

urlpatterns = format_suffix_patterns(urlpatterns)
