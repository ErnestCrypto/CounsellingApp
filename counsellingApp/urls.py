# creating urls
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'counsellingUrls'

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('login/', views.loginPage, name="loginPage"),
    path('ad/', views.adminPage, name="adminPage"),
    path('profile/', views.profilePage, name="profilePage"),

]

urlpatterns += staticfiles_urlpatterns()
