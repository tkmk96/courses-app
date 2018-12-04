from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
import datetime

from .models import Course, User
from .serializers import CourseSerializer, UserSerializer


class CourseViewSet(viewsets.ModelViewSet):

    def list(self, request):
        queryset = Course.objects.all()[:10]
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, id=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-name')
    serializer_class = UserSerializer

class TrendingViewSet(viewsets.ModelViewSet):
    time_24_hours_ago = datetime.datetime.now() - datetime.timedelta(days=1)
