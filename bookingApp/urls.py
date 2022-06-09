from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'bookingUrls'


urlpatterns = [
    path('', views.index, name='indexPage'),
    path('counselor/<int:object_id>/', views.details, name="details"),
    path('about/', views.about, name='aboutPage'),
    path('blog_single/', views.blog_single, name='blog_singlePage'),
    path('blog/', views.blog, name='blogPage'),
    path('contact/', views.contact, name='contactPage'),
    path('counselor/', views.counselor, name='counselorPage'),
    path('services/', views.services, name='servicesPage'),

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns = format_suffix_patterns(urlpatterns)
