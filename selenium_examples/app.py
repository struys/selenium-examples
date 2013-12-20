import os
import sqlite3
from flask import render_template
from flask import Flask

app = Flask(
	__name__,
	template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '', '../templates')
)

def with_cursor(func):

	def wrapped(self, *args, **kwargs):
		conn = sqlite3.connect('example.db')
		cursor = conn.cursor()

		try:
			return func(self, cursor, *args, **kwargs)
		finally:
			conn.commit()
			conn.close()

	return wrapped

class DB(object):

	@with_cursor
	def get_user(self, cursor, user_id):
		cursor.execute("""
			SELECT * from user where user.id = ?
		""", (user_id,))
		t = cursor.fetchone()
		return self.format_user_tuple(t)

	@with_cursor
	def get_user_by_email(self, cursor, email):
		cursor.execute("""
			SELECT * from user where user.email = ?
		""", (email,))
		t = cursor.fetchone()
		return self.format_user_tuple(t)

	@with_cursor
	def get_users(self, cursor):
		cursor.execute("""
			SELECT * from user
		""")

		return cursor.fetchall()

	@with_cursor
	def create_user(self, cursor, name, email, password):
		cursor.execute("""
			INSERT INTO user VALUES (?, ?, ?, ?)
		""", (None, name, email, password))


	@with_cursor
	def initialize_schema(self, cursor):
		cursor.execute("""
			CREATE TABLE user (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name TEXT,
				email TEXT,
				password TEXT
			)
		""")

	@staticmethod
	def format_user_tuple(t):
		return {
			'id': t[0],
			'name': t[1],
			'email': t[2],
			'password': t[3],
		}

class View(object):

	def render_template(self, name, **args):
		return render_template(name, **args)

db = DB()
view = View()


