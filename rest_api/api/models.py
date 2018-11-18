from django.db import models


# Category has name and courses
class Category(models.Model):
    name = models.CharField(max_length=128)


# Each Course belongs to 1 Category
class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    price = models.DecimalField(max_digits=5, decimal_places=2)


# User has UNIQUE name
class User(models.Model):
    name = models.CharField(max_length=128, unique=True)


# M : N relationship
# represents ownership of course
# date is created when entity is saved
# rating can be null
class CourseUser(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    date = models.DateField(auto_now_add=True)
    rating = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('course', 'user')


# Recommending based on similarity in description and name
# Recommended courses need to be in the same category
class RecommendationSimilarCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='rec_similar')
    recommended_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_offered')
    number = models.IntegerField()


# Recommending based on users' ownership
# For every user who bought certain course - counts occurrences of courses: (is there = +1)
# top X courses are selected
class RecommendationPeopleBuy(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='rec_bought')
    recommended_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_offered2')
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

