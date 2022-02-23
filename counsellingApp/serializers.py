# Creating serializers for the models
from rest_framework import serializers
from .models import Counsellor, SuperCounsellor, Achievement, Availability, Education, Experience, Therapy, Specialities, Login, Bookings


class CounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsellor
        fields = [
            'about',
            'title',
            'firstName',
            'lastName',
            'occupation',
            'gender',
            'email',
            'contact',
            'profile',
            'pin',
            'user_id',
            'status',
        ]
