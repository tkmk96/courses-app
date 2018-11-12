from django.contrib import admin
from .models import Course, CourseUser, User, RecommendationForUser, RecommendationSimilarCourse, RecommendationPeopleBuy

admin.site.register(Course)
admin.site.register(CourseUser)
admin.site.register(User)
admin.site.register(RecommendationForUser)
admin.site.register(RecommendationSimilarCourse)
admin.site.register(RecommendationPeopleBuy)
