# creating urls
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'counsellingUrls'

urlpatterns = [
    path('', views.homePage, name="homePage"),

]


urlpatterns += staticfiles_urlpatterns()
