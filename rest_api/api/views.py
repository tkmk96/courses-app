import datetime

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import detail_route, action
from rest_framework.response import Response

from .models import Course, User, CourseUser
from .serializers import CourseSerializer, UserSerializer, CourseUserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(methods=['get'], detail=True)
    def my_courses(self, request, pk):
        queryset = CourseUser.objects.filter(user_id=pk)
        serializer = CourseUserSerializer(queryset, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-name')
    serializer_class = UserSerializer


class CourseUserViewSet(viewsets.ModelViewSet):
    queryset = CourseUser.objects.all()
    serializer_class = CourseUserSerializer


class TrendingViewSet(viewsets.ModelViewSet): #9549
    ThirtyDaysAgo = datetime.date.today() - datetime.timedelta(days=60)
    queryset = sorted(CourseUser.objects.filter(date__gte=ThirtyDaysAgo)[:10], key=lambda t: t.ratingsCount, reverse=True)
    serializer_class = CourseUserSerializer

