from .models import Course, User, CourseUser, RecommendationPeopleBuy, RecommendationSimilarCourse, RecommendationForUser
from rest_framework import viewsets
from .serializers import CourseSerializer, UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('-name')
    serializer_class = CourseSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-name')
    serializer_class = UserSerializer
