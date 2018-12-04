from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Course, User, CourseUser
from .serializers import CourseSerializer, UserSerializer, CourseUserSerializer
import datetime
from django.db.models import Count



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
    ThirtyDaysAgo = datetime.datetime.now() - datetime.timedelta(days=30)
    queryset = sorted(CourseUser.objects.filter(date__gte=ThirtyDaysAgo)[:30], key=lambda t: t.ratingsCount, reverse=True)

    serializer_class = CourseUserSerializer

