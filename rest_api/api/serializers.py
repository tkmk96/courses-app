from .models import Category, Course, User, CourseUser, RecommendationPeopleBuy, RecommendationSimilarCourse, RecommendationForUser
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'courses')


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'category', 'name', 'description', 'price', 'rating', 'ratingsCount')


class UserSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'courses')
