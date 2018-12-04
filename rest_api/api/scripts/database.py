import os
import sqlite3


class Database:
    def __init__(self, dat_file):
        self.file_path = dat_file
        self.connection, self.cursor = None, None
        self.db_connect()

    def db_connect(self):
        self.connection = sqlite3.connect(self.file_path)
        self.cursor = self.connection.cursor()
        print("Database connected: " + os.path.abspath(self.file_path))

    def close(self):
        self.connection.commit()
        self.connection.close()

    def commit(self):
        self.connection.commit()

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

    def delete_users(self):
        query = "DELETE FROM api_user"
        self.cursor.execute(query)

    def delete_courses(self):
        query = "DELETE FROM api_course"
        self.cursor.execute(query)

    def delete_course_users(self):
        query = "DELETE FROM api_courseuser"
        self.cursor.execute(query)

    def delete_all(self):
        self.delete_course_users()
        self.delete_users()
        self.delete_courses()
