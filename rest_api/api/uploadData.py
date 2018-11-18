import csv
from api.models import Course, Category, CourseUser, User, RecommendationForUser, RecommendationSimilarCourse, RecommendationPeopleBuy


#TO RUN SCRIPT
#\courses\courses-app\rest_api>python manage.py shell
#exec(open("./api/uploadData.py").read())

User.objects.all().delete()
with open('api/csv/Users.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    line_count = 0
    for row in reader:
        if line_count != 0:
            obj = User(name=row[0])
            obj.save()
        if line_count % 100 == 0:
        	print('User line: ' + str(line_count))
        line_count += 1


Category.objects.all().delete()
with open('api/csv/Category.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    line_count = 0
    for row in reader:
        if line_count != 0:
            obj = Category(name=row[0])
            obj.save()
        line_count += 1


# obj = Course(category=all[0], name='test', description='test', price=122)

Course.objects.all().delete()
with open('api/csv/Course.csv', encoding="utf8") as f:
    reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in reader:
        if line_count != 0:
            obj = Course(
            	category=Category.objects.filter(name=row[7])[0],
            	name=row[0],
            	description=row[1],
            	price=row[6]
            )
            obj.save()
        if line_count != 0:
        	print('Course line: ' + str(line_count))
        line_count += 1

CourseUser.objects.all().delete()
with open('api/csv/CourseUser.csv', encoding="utf8") as f:
    reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in reader:
        if line_count != 0:
            tmp = Course.objects.filter(name=row[2])
            tmp2 = User.objects.filter(name=row[1])
            if len(tmp) != 0 and len(tmp2) != 0: 
                obj = CourseUser(
                	course=tmp[0],
                	user=tmp2[0],
                	rating=row[0]
                )
                try:
                    obj.save()
                except:
                    print('Error line: ' + str(line_count))
        if line_count:
        	print('CourseUser line: ' + str(line_count))
        line_count += 1
