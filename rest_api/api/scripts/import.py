
# INSTRUCTIONS
# to run script: py ./import.py ../../db.sqlite3

from sys import argv
from csv import reader
import random
import time
# noinspection PyUnresolvedReferences
from database import Database


CSV_PATH = '../csv/'
CSV_USERS = 'Users.csv'
CSV_COURSE = 'Course.csv'
CSV_COURSE_USER = 'CourseUser.csv'
CSV_KEYWORDS = 'KeyWords.csv'


def get_csv_path(csv):
    return CSV_PATH + csv


def get_progress(current, total):
    return str(current) + ' / ' + str(total)


def get_random_date(start, end):
    time_format = '%Y/%m/%d %H:%M'
    start_time = time.mktime(time.strptime(start, time_format))
    end_time = time.mktime(time.strptime(end, time_format))
    random_time = start_time + random.random() * (end_time - start_time)

    return time.strftime(time_format, time.localtime(random_time))


def get_users_dict():
    with open(get_csv_path(CSV_USERS), encoding="utf8") as file:
        csv = reader(file)
        next(csv)
        data = dict()
        for row in csv:
            data[row[0]] = -1
        return data


def get_courses_dict():
    with open(get_csv_path(CSV_COURSE), encoding="utf8") as file:
        csv = reader(file)
        next(csv)
        data = dict()
        for row in csv:
            data[row[0]] = {
                'id': -1,
                'description': row[1],
                'price': row[6],
                'lectures': int(row[3]) if row[3] != '' else 0,
                'difficulty':row[4],
            }
        return data


def get_keywords():
    with open(get_csv_path(CSV_KEYWORDS), encoding="utf8") as file:
        csv = reader(file)
        next(csv)
        data = []
        for row in csv:
            data.append(row[0])
        return data


def get_course_users(users, courses):
    with open(get_csv_path(CSV_COURSE_USER), encoding="utf8") as file:
        csv = reader(file)
        next(csv)
        data = dict()
        skipped = 0
        for row in csv:
            try:
                user_id = users[row[1]]
                course_id = courses[row[2]]['id']
                key = str(user_id) + ':' + str(course_id)
                rating = row[0]
                date = get_random_date('2010/01/01 00:01', '2018/10/30 23:59')
                data[key] = {
                    'user': user_id,
                    'course': course_id,
                    'rating': rating,
                    'date': date
                }
            except KeyError:
                skipped +=1
        print('Skipped: ' + str(skipped))
        return data


def save_users(db, users):
    total = len(users)
    current = 1
    skipped = 0
    for user in users.keys():
        user_id = db.insert_user(user)
        users[user] = user_id
        print("Saving users: " + get_progress(current, total), end='\r')
        current += 1
    print("Saving users finished!")


def save_courses(db, courses):
    total = len(courses)
    current = 1
    for name, course in courses.items():
        course_id = db.insert_course(name, course)
        courses[name]['id'] = course_id
        print("Saving courses: " + get_progress(current, total), end='\r')
        current += 1
    print("Saving courses finished!")


def save_course_user(db, course_users):
    total = len(course_users)
    current = 1
    for course_user in course_users.values():
        db.insert_course_user(course_user)
        print("Saving course_users: " + get_progress(current, total), end='\r')
        current += 1
    print("Saving course_users finished!")


def save_keywords(db, keywords):
    total = len(keywords)
    current = 1
    skipped = 0
    data = dict()
    for kw in keywords:
        data[kw] = db.insert_keyword(kw)
        print("Saving keywords: " + get_progress(current, total), end='\r')
        current += 1
    print("Saving keywords finished!")
    return data


def main():
    if len(argv) < 2:
        print("Path to database need to be passed as the first argument!")
        exit(-1)
    db_path = argv[1]
    db = Database(db_path)

    # clear all tables
    db.delete_all()
    db.commit()

    # saving keywords
    keywords = save_keywords(db, get_keywords())

    # saving users
    users = get_users_dict()
    save_users(db, users)

    # saving courses
    courses = get_courses_dict()
    save_courses(db, courses)

    # saving course users
    course_users = get_course_users(users, courses)
    save_course_user(db, course_users)
    db.close()


if __name__ == '__main__':
    main()
