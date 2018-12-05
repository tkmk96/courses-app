from sys import argv
# noinspection PyUnresolvedReferences
from database import Database

# INSTRUCTIONS
# to run script: py ./recmake.py ../../db.sqlite3 [1 | 2 | 3 | 0]

ALL = 0
PEOPLE_BUY = 1
SIMILAR = 2
FOR_USER = 3


def get_progress(current, total):
    return str(current) + ' / ' + str(total)


def similar_courses(db):
    db.delete_rec_similar()
    courses = db.get_all_courses()
    skipped = 0
    for course_id, course in courses.items():
        others = db.get_similar_courses(course_id)
        if len(others.keys()) < 1:
            skipped += 1
            continue
        result = []
        lectures = course['lectures'] != 0
        for other_id, other in others.items():
            rating = other['match'] * 100
            if course['difficulty'] == other['difficulty']:
                rating += 30
            if lectures and other['lectures'] != 0:
                lratio = course['lectures'] / other['lectures']
                if 0.7 < lratio < 1.3:
                    rating += 10
            pratio = course['price'] / other['price']
            if 0.7 < pratio < 1.3:
                rating += 25
            result.append((other_id, rating))
        result = sorted(result, key=lambda k: k[1], reverse=True)
        result = result[:3]
        for index, rec in enumerate(result):
            db.insert_rec_similar_courses(course_id, rec[0], index)
    db.commit()
    print('Similar - skipped: ' + str(skipped) + ' / ' + str(len(courses.keys())))


def people_buy(db):
    db.delete_rec_people_buy()
    courses_users = db.get_all_courses_with_users()
    skipped = 0
    # process course
    for course_id, course in courses_users.items():
        others = dict()
        # process users of course
        for user in course['users']:
            other_courses = db.get_user_courses_except(user['id'], course_id)
            for other_id in other_courses:
                if others.get(other_id):
                    others[other_id] += 1
                else:
                    others[other_id] = 1
        if len(others.keys()) < 1:
            skipped += 1
            continue
        # sort occurrences
        others_sorted = []
        for rec_id, count in others.items():
            others_sorted.append((rec_id, count))
        others_sorted.sort(key=lambda x: x[1], reverse=True)

        if len(others_sorted) > 3:
            others_sorted = others_sorted[:3]
        for index, rec in enumerate(others_sorted):
            db.insert_rec_people_buy(course_id, rec[0], index)
    db.commit()
    print('People buy - skipped courses: ' + str(skipped) + ' / ' + str(len(courses_users.keys())))


def for_user(db):
    db.delete_rec_for_user()
    users = db.get_all_users()
    skipped = 0
    current = 1
    total = len(users.keys())
    for user_id, courses in users.items():
        other = dict()
        for course_id in courses:
            c_users = db.get_course_users(course_id)
            for u in c_users:
                uc = db.get_user_courses(u)
                for cid in uc:
                    if other.get(cid) is None:
                        other[cid] = 1
                    else:
                        other[cid] += 1
        if len(other.keys()) < 1:
            skipped += 1
            continue
        result = sorted(other.items(), key=lambda k: k[1], reverse=True)
        result = result[:3]
        for index, rec in enumerate(result):
            db.insert_rec_for_user(user_id, rec[0], index)
        print("For users: " + get_progress(current, total), end='\r')
        current += 1
    db.commit()
    print('For user - skipped users: ' + str(skipped) + ' / ' + str(total))


def process_mode(db, mode):
    if mode == PEOPLE_BUY:
        people_buy(db)
    elif mode == SIMILAR:
        similar_courses(db)
    elif mode == FOR_USER:
        for_user(db)
    elif mode == ALL:
        people_buy(db)
        similar_courses(db)
        for_user(db)


def main():
    if len(argv) >= 3:
        mode = int(argv[2])
    else:
        mode = 0
    dat_file = argv[1]
    db = Database(dat_file)
    process_mode(db, mode)

    db.close()


if __name__ == '__main__':
    main()

# def write_key_words_csv(db):
#     with open('KeyWords.csv', 'w', newline='', encoding='utf8') as file:
#         fieldnames = ['keyword']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         words = db.get_keywords()
#         for w in words:
#             writer.writerow({'keyword': w})
#
#
# def get_word_count(courses):
#     keywords = {}
#     for _, course in courses.items():
#         names = course['name'].split()
#         for n in names:
#             if len(n) < 3:
#                 continue
#             if keywords.get(n) is None:
#                 keywords[n] = 0
#             keywords[n] += 1
#     for key in list(keywords.keys()):
#         if keywords[key] < 2:
#             del keywords[key]
#             continue
#     sorted_keywords = sorted(keywords.items(), key=lambda k: k[1], reverse=True)
#     return sorted_keywords
