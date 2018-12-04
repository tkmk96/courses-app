from sys import argv
# noinspection PyUnresolvedReferences
from database import Database

ALL = 0
PEOPLE_BUY = 1


def people_buy(db):
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
    print('People buy skipped courses: ' + str(skipped) + ' / ' + str(len(courses_users.keys())))


def process_mode(db, mode):
    if mode == PEOPLE_BUY:
        people_buy(db)


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
