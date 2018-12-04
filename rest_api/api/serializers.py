from .models import Course, User, CourseUser, RecommendationPeopleBuy, RecommendationSimilarCourse, RecommendationForUser
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'price', 'rating', 'ratingsCount')


class UserSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'courses')

class CourseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseUser
        fields = ('id', 'course', 'user', 'date', 'rating', 'ratingsCount')
