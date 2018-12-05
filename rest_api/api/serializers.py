from .models import Course, User, CourseUser, RecommendationPeopleBuy, RecommendationSimilarCourse, RecommendationForUser
from rest_framework import serializers



class RecommendationPeopleBuySerializer(serializers.ModelSerializer):

    class Meta:
        model = RecommendationPeopleBuy
        fields = ('recommended_course',)


class CourseSerializer(serializers.ModelSerializer):
    recommendBuy = RecommendationPeopleBuySerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'price', 'rating', 'ratingsCount',
                  'lectures', 'difficulty', 'recommendBuy')


class UserSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'courses')

class CourseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseUser
        fields = ('course', 'name', 'description', 'ratingsCount')
