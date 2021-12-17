# creating views
from django.http import request
from django.shortcuts import render


def homePage(request):

    profile = 'app/profile.html'
    notification = 'app/notification.html'
    index = 'app/index.html'
    return render(request, 'app/home.html', {'profile': profile,
                                             'notification': notification,
                                             'index': index,
                                             })
