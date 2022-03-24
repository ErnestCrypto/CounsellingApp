from django import views
from .serializers import CounsellorSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Counsellor


@api_view(['GET', 'PUT', 'DELETE'])
def counsellor_details(request, pk):

    try:
        counsellor = Counsellor.objects.get(user_id=pk)
    except counsellor.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = CounsellorSerializer(counsellor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CounsellorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        counsellor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def counsellor_list(request):
    if request.method == 'GET':
        counsellor = Counsellor.objects.all()
        serializer = CounsellorSerializer(counsellor, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CounsellorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CounsellorList(views.View):
#     def get(self, request):
#         counsellor = Counsellor.objects.all()
#         serializer = CounsellorSerializer(counsellor, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CounsellorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
