import os
import sqlite3


class Database:
    def __init__(self, dat_file):
        self.file_path = dat_file
        self.connection, self.cursor = None, None
        self.db_connect()

    # MANAGE CONNECTION
    def db_connect(self):
        self.connection = sqlite3.connect(self.file_path)
        self.cursor = self.connection.cursor()
        print("Database connected: " + os.path.abspath(self.file_path))

    def close(self):
        self.connection.commit()
        self.connection.close()

    def commit(self):
        self.connection.commit()

    # INSERTS
    def insert_user(self, name):
        query = "INSERT INTO api_user(name) VALUES (?)"
        params = (name,)
        self.cursor.execute(query, params)
        return self.cursor.lastrowid

    def insert_course(self, name, course):
        query = "INSERT INTO api_course(name, description, price, lectures, difficulty) VALUES (?, ?, ?, ?, ?)"
        params = (name, course['description'], course['price'], course['lectures'], course['difficulty'])
        self.cursor.execute(query, params)
        return self.cursor.lastrowid

    def insert_course_user(self, course_user):
        query = "INSERT INTO api_courseuser(course_id, user_id, rating, date) VALUES (?, ?, ?, ?)"
        params = (course_user['course'], course_user['user'], course_user['rating'], course_user['date'])
        self.cursor.execute(query, params)
        return self.cursor.lastrowid

    def insert_keyword(self, word):
        query = "INSERT INTO api_keyword(word) VALUES (?)"
        params = (word,)
        self.cursor.execute(query, params)
        return self.cursor.lastrowid

    def insert_course_keyword(self, course_id, keyword_id):
        query = "INSERT INTO api_coursekeyword(course_id, keyword_id) VALUES (?, ?)"
        params = (course_id, keyword_id)
        self.cursor.execute(query, params)
        return self.cursor.lastrowid

    def insert_rec_people_buy(self, course_id, rec_id, number):
        query = "INSERT INTO api_recommendationpeoplebuy(course_id, recommended_course_id, number) VALUES (?, ?, ?)"
        params = (course_id, rec_id, number)
        self.cursor.execute(query, params)
        return self.cursor.lastrowid

    def insert_rec_similar_courses(self, course_id, rec_id, number):
        query = "INSERT INTO api_recommendationsimilarcourse(course_id, recommended_course_id, number) VALUES (?, ?, ?)"
        params = (course_id, rec_id, number)
        self.cursor.execute(query, params)
        return self.cursor.lastrowid

    # GETS
    # 0course_id 1name 2description 3price 4lectures 5difficulty 6- 7date 8rating 9-0 10user_id
    def get_all_courses_with_users(self):
        query = "SELECT * FROM api_course INNER JOIN api_courseuser a on api_course.id = a.course_id"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        result = dict()
        for row in rows:
            if result.get(row[0]) is None:
                result[row[0]] = {
                    'name': row[1],
                    'description': row[2],
                    'price': row[3],
                    'lectures': row[4],
                    'difficulty': row[5],
                    'users': []
                }
            user = {
                'id': row[10],
                'rating': row[8],
                'date': row[7],
            }
            result[row[0]]['users'].append(user)
        return result

    def get_user_courses_except(self, user_id, course_id):
        query = "SELECT course_id FROM api_courseuser WHERE user_id = ? and course_id != ?"
        params = (user_id, course_id)
        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()
        result = []
        for row in rows:
            result.append(row[0])
        return result

    def get_similar_courses(self, course_id):
        query = """SELECT course_id, keyword_id, name, description, price, difficulty, lectures FROM
                  (SELECT course_id, keyword_id FROM api_coursekeyword WHERE course_id != ? AND keyword_id IN
                          (SELECT keyword_id FROM api_coursekeyword WHERE course_id = ?))
                   INNER JOIN api_course on id = course_id
        """.strip()
        params = (course_id, course_id)
        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()
        result = {}
        for row in rows:
            if result.get(row[0]) is None:
                result[row[0]] = {
                    'name': row[2],
                    'description': row[3],
                    'price': row[4],
                    'lectures': row[6],
                    'difficulty': row[5],
                    'match': 0
                }
            result[row[0]]['match'] += 1
        return result

    def get_all_courses(self):
        query = "SELECT * FROM api_course"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        result = dict()
        for row in rows:
            result[row[0]] = {
                'name': row[1],
                'description': row[2],
                'price': row[3],
                'lectures': row[4],
                'difficulty': row[5],
            }
        return result

    def get_keywords(self):
        query = "SELECT word FROM api_keyword"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        result = []
        for row in rows:
            result.append(row[0])
        return result

    # DELETES
    def delete_users(self):
        query = "DELETE FROM api_user"
        self.cursor.execute(query)

    def delete_courses(self):
        query = "DELETE FROM api_course"
        self.cursor.execute(query)

    def delete_course_users(self):
        query = "DELETE FROM api_courseuser"
        self.cursor.execute(query)

    def delete_course_keywords(self):
        query = "DELETE FROM api_coursekeyword"
        self.cursor.execute(query)

    def delete_keywords(self):
        query = "DELETE FROM api_keyword"
        self.cursor.execute(query)

    def delete_rec_people_buy(self):
        query = "DELETE FROM api_recommendationpeoplebuy"
        self.cursor.execute(query)

    def delete_rec_similar(self):
        query = "DELETE FROM api_recommendationsimilarcourse"
        self.cursor.execute(query)

    def delete_all(self):
        self.delete_course_users()
        self.delete_course_keywords()
        self.delete_users()
        self.delete_courses()
        self.delete_keywords()
        self.delete_rec_people_buy()
        self.delete_rec_similar()
