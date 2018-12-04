from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Course, User, CourseUser
from .serializers import CourseSerializer, UserSerializer, CourseUserSerializer
import datetime
from django.db.models import Count
from django.db.models import Q


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

class TrendingViewSet(viewsets.ModelViewSet): #9549
    ThirtyDaysAgo = datetime.datetime.now() - datetime.timedelta(days=7)
    #queryset = CourseUser.objects.filter(date__gte=ThirtyDaysAgo).annotate(count=Count('course', filter=Q(course=9549))).order_by('-count')[:10]
    queryset = CourseUser.objects.filter(date__gte=ThirtyDaysAgo).annotate(count=Count('course')).order_by('-count')[:10]

    serializer_class = CourseUserSerializer

