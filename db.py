import sqlite3

# password storage database


class DB:
	def __init__(self, path):
		self.db = sqlite3.connect(path)
		self.cursor = self.db.cursor()


	def create_table(self):
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS passwords (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				name VARCHAR(255) NOT NULL,
				login VARCHAR(255) NOT NULL,
				password VARCHAR(255) NOT NULL,
				url VARCHAR(255),
				notes VARCHAR(255)
			)
		""")

		self.db.commit()


	def add_password(self, name, login, password, url, notes):
		self.cursor.execute("""
			INSERT INTO passwords (name, login, password, url, notes)
			VALUES (?, ?, ?, ?, ?)
		""", (name, login, password, url, notes))
		self.db.commit()


	def get_passwords(self):
		self.cursor.execute("SELECT * FROM passwords")
		return self.cursor.fetchall()
	

	def delete_password(self, id):
		self.cursor.execute("DELETE FROM passwords WHERE id=?", (id,))
		self.db.commit()


	def update_password(self, id, name, login, password, url, notes):
		self.cursor.execute("""
			UPDATE passwords
			SET name=?, login=?, password=?, url=?, notes=?
			WHERE id=?
		""", (name, login, password, url, notes, id))
		self.db.commit()


	def get_password_by_id(self, id):
		self.cursor.execute("SELECT * FROM passwords WHERE id=?", (id,))
		return self.cursor.fetchone()
	
	def page_count(self):
		self.cursor.execute("SELECT COUNT(*) FROM passwords")
		return self.cursor.fetchone()[0]
	
	def pass_count(self):
		self.cursor.execute("SELECT COUNT(*) FROM passwords")
		return self.cursor.fetchone()[0]
	
	def search_by_name(self, name):
		self.cursor.execute("SELECT * FROM passwords WHERE name=?", (name,))
		return self.cursor.fetchall()
	
	def search_by_login(self, login):
		self.cursor.execute("SELECT * FROM passwords WHERE login=?", (login,))
		return self.cursor.fetchall()
	
	def search_by_url(self, url):
		self.cursor.execute("SELECT * FROM passwords WHERE url=?", (url,))
		return self.cursor.fetchall()
	
	def paginate(self, page, limit=1):
		return self.cursor.execute("SELECT * FROM passwords LIMIT ? OFFSET ?", (limit, (page-1)*limit)).fetchall()

	def __del__(self):
		self.db.close()


	def close(self):
		self.db.close()


