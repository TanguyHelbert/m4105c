import sqlite3

class DataBase:
	"""docstring for DataBase"""
	def __init__(self, path, name, items):
		self.path=path
		self.name=name
		self.items=items

	"""set the name of the data base"""
	def setName(self, name):
		self.name=name

	"""get the name of the data base"""
	def getName(self):
		return self.name

	"""set the list of items"""
	def setItems(self, items):
		self.items=items

	"""open the connection"""
	def open(self):
		return sqlite3.connect(self.path)

	"""create the table"""
	def table(self):
		conn = self.open()
		c = conn.cursor()
		print("insertDB")
		c.execute("DROP TABLE IF EXISTS " + self.name)
		c.execute(self.items[0].sql_create())
		conn.commit()
		self.close(conn)

	"""do a loop to insert all items in the list in the table"""
	def insert(self):
		conn = self.open()
		c = conn.cursor()
		print(self.name)
		print("insertDB")
		for item in self.items:
			c.execute(item.sql_insert())

		conn.commit()
		self.close(conn)

	"""return all items in the list"""
	def selectAll(self):
		conn = self.open()
		c = conn.cursor()
		print(self.name)
		c.execute("SELECT * FROM " + self.name)
		liste = c.fetchall()
		#print(liste)
		return liste
		self.close(conn)

	"""return all items corresponding to the id"""
	def select(self, id):
		conn = self.open()
		c = conn.cursor()
		c.execute("SELECT * FROM " + self.name + " WHERE numb LIKE '%" + id + "%'")
		occurence = c.fetchall()
		return occurence
		self.close(conn)

	"""return all items corresponding to the parameters"""
	def selectSpecial(self, activity, cityy):
		conn = self.open()
		c = conn.cursor()
		cityyy = "'"+cityy+"'"
		c.execute("SELECT i.numb, i.name, e.numb, e.name, a.numb, a.name FROM Installation i JOIN Equipment e ON i.numb = e.numb2 JOIN Activity a ON e.numb = a.numb2 WHERE i.city = " + cityyy + " AND a.name LIKE '%" + activity + "%'")
		liste = c.fetchall()
		return liste
		self.close(conn)
	
	"""return the number of attributs in the table"""
	def countAttribut(self):
		conn = self.open()
		c = conn.cursor()
		c.execute("SELECT COUNT(*) FROM " + self.name)
		nb_Items = c.fetchone()[0]
		return nb_Items
		self.close(conn)

	"""close the connection"""
	def close(self, conn):
		conn.close()