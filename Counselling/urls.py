
from ast import pattern
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('counsellingApp.urls', namespace='counsellingUrls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


urlpatterns += [re_path(r'^%s/' %
                        settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
                ]

urlpatterns += staticfiles_urlpatterns()
