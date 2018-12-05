from django.db import models
from django.db.models import Avg, Count
import datetime


# Course has unique name
class Course(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.CharField(max_length=1024)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    lectures = models.IntegerField()
    difficulty = models.CharField(max_length=128)

    @property
    def rating(self):
        aggregate = CourseUser.objects.filter(course__id=self.id).aggregate(Avg('rating'))
        if aggregate['rating__avg'] is None:
            return 0
        return round(aggregate['rating__avg'], 1)

    @property
    def ratingsCount(self):
        aggregate = CourseUser.objects.filter(course__id=self.id).aggregate(Count('rating'))
        return aggregate['rating__count']


# User has UNIQUE name
class User(models.Model):
    name = models.CharField(max_length=128, unique=True)


class KeyWord(models.Model):
    word = models.CharField(max_length=64, unique=True)


# M : N relationship
# represents ownership of course
# date is created when entity is saved
# rating can be null
class CourseUser(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    date = models.DateField(auto_now_add=True)
    rating = models.FloatField(null=True, blank=True)

    @property
    def ratingsCount(self):
        ThirtyDaysAgo = datetime.date.today() - datetime.timedelta(days=60)
        count = CourseUser.objects.filter(date__gte=ThirtyDaysAgo).filter(course=self.course).count()
        return count

    @property
    def description(self):
        return self.course.description

    @property
    def name(self):
        return self.course.name

    class Meta:
        unique_together = ('course', 'user')


class CourseKeyword(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='keywords')
    keyword = models.ForeignKey(KeyWord, on_delete=models.CASCADE, related_name='kw_courses')

    class Meta:
        unique_together = ('course', 'keyword')


# Recommending based on similarity in description and name
class RecommendationSimilarCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='recommendSimilar')
    recommended_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_offered')
    number = models.IntegerField()


# Recommending based on users' ownership
# For every user who bought certain course - counts occurrences of courses: (is there = +1)
# top X courses are selected
class RecommendationPeopleBuy(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='recommendBuy')
    recommended_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='rec_course')
    number = models.IntegerField()


# Recommending bases on specific user's ownership
# Gets all his courses
# Gets users who bought all these courses
# counts occurrence of other courses from users
# top X courses are selected
class RecommendationForUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')
    recommended_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.IntegerField()




