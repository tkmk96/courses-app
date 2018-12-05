from sys import argv
# noinspection PyUnresolvedReferences
from database import Database
import csv

ALL = 0
PEOPLE_BUY = 1
SIMILAR = 2


def write_key_words(db):
    with open('KeyWords.csv', 'w', newline='', encoding='utf8') as file:
        fieldnames = ['keyword']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        words = db.get_keywords()
        for w in words:
            writer.writerow({'keyword': w})


def get_word_count(courses):
    keywords = {}
    for _, course in courses.items():
        names = course['name'].split()
        for n in names:
            if len(n) < 3:
                continue
            if keywords.get(n) is None:
                keywords[n] = 0
            keywords[n] += 1
    for key in list(keywords.keys()):
        if keywords[key] < 2:
            del keywords[key]
            continue
    sorted_keywords = sorted(keywords.items(), key=lambda k: k[1], reverse=True)
    return sorted_keywords


def similar_courses(db):
    #db.delete_rec_similar()
    #courses = db.get_all_courses()
    #words = get_word_count(courses)
    write_key_words(db)



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


def process_mode(db, mode):
    if mode == PEOPLE_BUY:
        people_buy(db)
    elif mode == SIMILAR:
        similar_courses(db)


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
