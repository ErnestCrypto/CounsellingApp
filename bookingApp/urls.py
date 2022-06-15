from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from counsellingApp import views as coun_views

app_name = 'bookingUrls'


urlpatterns = [
    path('', coun_views.loginPage, name='loginPage'),
    path('send/<int:pk>/', views.send, name='send'),
    path('book/<int:pk>/<int:object_user_id>/', views.book, name='book'),
    path('logout/<int:pk>/', views.logout, name='logout'),
    path('index/<int:pk>/', views.index, name='indexPage'),
    path('bookings/<int:pk>/', views.bookings, name='bookings'),
    path('delete/<int:booking_id>/', views.delete, name='delete'),
    path('counselor/<int:object_id>/', views.details, name="details"),
    path('about/', views.about, name='aboutPage'),
    path('blog_single/', views.blog_single, name='blog_singlePage'),
    path('blog/', views.blog, name='blogPage'),
    path('contact/', views.contact, name='contactPage'),
    path('counselor/', views.counselor, name='counselorPage'),
    path('services/', views.services, name='servicesPage'),
    path('dashboard/<str:pk>/', views.dashboard, name='dashboard'),

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns = format_suffix_patterns(urlpatterns)
