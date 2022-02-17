# creating urls
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'counsellingUrls'

urlpatterns = [
    path('', views.loginPage, name="loginPage"),
    path('search/<str:pk>/', views.search, name="search"),
    path('dashboard/<str:pk>/', views.adminPage, name="adminPage"),
    path('admindashboard/<str:pk>/', views.superadminPage, name="superadminPage"),
    path('admindashboard/<str:pk>/', views.superadminPage, name="superadminPage"),
    path('admindashboard/<str:pk>/', views.superadminPage, name="superadminPage"),
    path('admindashboard/<str:pk>/', views.superadminPage, name="superadminPage"),

    path('home/<str:pk>/', views.homePage, name="homePage"),
    path('notifications/<str:pk>/',
         views.notificationPage, name="notificationPage"),
    path('index/<str:pk>/',
         views.indexPage, name="indexPage"),

    path('profile/<str:pk>/', views.profilePage, name="profilePage"),
    path('delete/<str:studentbook_id>/', views.delete, name="delete"),
    path('update/<str:studentbook_id>/<str:studentbook_status>',
         views.update, name="update"),


]

urlpatterns += staticfiles_urlpatterns()
