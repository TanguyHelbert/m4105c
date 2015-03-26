import sqlite3

class DataBase:
	def __init__(self, path, name, items):
		self.path=path
		self.name=name
		self.items=items

	def setName(self, name):
		self.name=name

	def getName(self):
		return self.name

	def setItems(self, items):
		self.items=items

	def open(self):
		return sqlite3.connect(self.path)

	def table(self):
		conn = self.open()
		c = conn.cursor()
		print("insertDB")
		c.execute("DROP TABLE IF EXISTS " + self.name)
		c.execute(self.items[0].sql_create())
		conn.commit()
		self.close(conn)

	def insert(self):
		conn = self.open()
		c = conn.cursor()
		print(self.name)
		print("insertDB")
		for item in self.items:
			c.execute(item.sql_insert())

		conn.commit()
		self.close(conn)

	def selectAll(self):
		conn = self.open()
		c = conn.cursor()
		print(self.name)
		c.execute("SELECT * FROM " + self.name + " LIMIT 10")
		liste = c.fetchall()
		#print(liste)
		return liste
		self.close(conn)

	def select(self, id):
		conn = self.open()
		if self.name=="equipment":
			colonne="InsNum"
		elif self.name=="activity":
			colonne="EquipmentId"
		else:
			colonne="numb"

		c = conn.cursor()
		c.execute("SELECT * FROM " + self.name + " WHERE " + colonne + " LIKE '%" + id + "%'")
		occurence = c.fetchall()
		return occurence
		self.close(conn)

	def countAttribut(self):
		conn = self.open()
		c = conn.cursor()
		c.execute("SELECT COUNT(*) FROM " + self.name)
		nbItems = c.fetchone()[0]
		return nbItems
		self.close(conn)

	def close(self, conn):
		conn.close()