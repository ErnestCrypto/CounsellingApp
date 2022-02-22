# creating urls
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

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
    path('profile/<str:pk>/', views.profilePage, name="profilePage"),
    path('delete/<str:studentbook_id>/', views.delete, name="delete"),
    path('update/<str:studentbook_id>/<str:studentbook_status>',
         views.update, name="update"),
    path('availability_del/<str:av_id>',
         views.availability_del, name="availability_del"),
    path('availability_add/<str:av_id>',
         views.availability_add, name="availability_add"),


]

urlpatterns += staticfiles_urlpatterns()
