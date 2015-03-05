import sqlite3

class DataBase:
	def __init__(self, path, name, items):
		self.conn=sqlite3.connect(path)
		self.name=name
		self.items=items

	def setName(self, name):
		self.name = name

	def setItems(self, items):
		self.items = items

	def table(self):
		c = self.conn.cursor()
		c.execute("DROP TABLE IF EXISTS " + self.name)
		c.execute(self.items[0].sql_create())
		self.conn.commit()

	def close(self):
		self.conn.close()

	def insert(self):
		c = self.conn.cursor()
		for item in self.items:
			c.execute(item.sql_insert())

		self.conn.commit()

	def selectAll(self):
		c = self.conn.cursor()
		liste = c.execute("SELECT * FROM " + self.name)
		return liste
