#nomville
#nomactivite

# heure de passage 10h50
# C0/04 C0/05

import cherrypy
import model.dataBase as db
from mako.template import Template

#localhost:8080
#localhost:8080/show_all

liste_fake = []
data = db.DataBase("dataBase.db", "Equipment", liste_fake)

class WebManager(object):
	"""
	Exposes web services
	"""
	@cherrypy.expose
	def index(self):
		"""
		Exposes the service at localhost:8080/
		"""
		viewB = Template(filename="services/html/header.html")
		viewE = Template(filename="services/html/footer.html")
		viewI1 = Template(filename="services/html/firstView.html")
		html = (viewB.render())
		html += (viewI1.render())
		html += (viewE.render())
		return html

	@cherrypy.expose
	def show_allEquipment(self):
		"""
		Exposes the service at localhost:8080/show_all/
		"""
		data.setName("Equipment")
		viewB = Template(filename="services/html/header.html")
		viewE = Template(filename="services/html/footer.html")
		html = (viewB.render())
		html += "<h2>List of all elements in the table "+data.getName()+"</h2>"
		html += "<a href=\"javascript:history.go(-1)\">return</a>"
		html += "<table border=1><th colspan=\"2\">"+data.getName()+"</th><tr>"
		html += "<td>Name of the equipment</td><td>Number of the equipment</td></tr><tr>"
		html += "<td></td><td></td></tr><tr>"
		for i in data.selectAll():
			html += "<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>"
		html += "</table>"
		html += (viewE.render())
		return html

	@cherrypy.expose
	def show_allActivity(self):
		"""
		Exposes the service at localhost:8080/show_all/
		"""
		data.setName("Activity")
		viewB = Template(filename="services/html/header.html")
		viewE = Template(filename="services/html/footer.html")
		html = (viewB.render())
		html += "<h2>List of all elements in the table "+data.getName()+"</h2>"
		html += "<a href=\"javascript:history.go(-1)\">return</a>"
		html += "<table border=1><th colspan=\"2\">"+data.getName()+"</th><tr>"
		html += "<td>Name of the sport</td><td>Number of the equipment</td></tr><tr>"
		html += "<td></td><td></td></tr><tr>"
		for i in data.selectAll():
			html += "<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>"
		html += "</table>"
		html += (viewE.render())
		return html

	@cherrypy.expose
	def show_allInstallation(self):
		"""
		Exposes the service at localhost:8080/show_all/
		"""
		data.setName("Installation")
		viewB = Template(filename="services/html/header.html")
		viewE = Template(filename="services/html/footer.html")
		html = (viewB.render())
		html += "<h2>List of all elements in the table "+data.getName()+"</h2>"
		html += "<a href=\"javascript:history.go(-1)\">return</a>"
		html += "<table border=1><th colspan=\"5\">"+data.getName()+"</th><tr>"
		html += "<td>Name of the Installation</td><td>Number of the Installation</td><td>Address</td><td>Postal Code</td><td>City</td></tr><tr>"
		html += "<td></td><td></td></tr><tr>"
		for i in data.selectAll():
			html += "<td>"+i[0]+"</td><td>"+i[1]+"</td><td>"+i[2]+"</td><td>"+i[3]+"</td><td>"+i[4]+"</td></tr><tr>"
		html += "</table>"
		html += (viewE.render())
		return html

	@cherrypy.expose
	def showEquipment(self, id):
		"""
		Exposes the service at localhost:8080/show/[id]/
		"""
		try:
			data.setName("Equipment")
			viewB = Template(filename="services/html/header.html")
			viewE = Template(filename="services/html/footer.html")
			html = (viewB.render())
			html += "<h2>Search in the table Equipment</h2>"
			html += "<a href=\"javascript:history.go(-1)\">return</a>"
			html += "<table border=1><th colspan=\"2\">"+data.getName()+"</th><tr>"
			html += "<td>Name of the equipment</td><td>Number of the equipment</td></tr><tr>"
			html += "<td></td><td></td></tr><tr>"
			for i in data.select(id):
				html += "<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>"
			html += "</table>"
		except (IndexError, IOError):
			return "Invalid ID"

		return html

	@cherrypy.expose
	def showActivity(self, id):
		"""
		Exposes the service at localhost:8080/show/[id]/
		"""
		try:
			data.setName("Activity")
			viewB = Template(filename="services/html/header.html")
			viewE = Template(filename="services/html/footer.html")
			html = (viewB.render())
			html += "<h2>Search in the table Activity</h2>"
			html += "<a href=\"javascript:history.go(-1)\">return</a>"
			html += "<table border=1><th colspan=\"2\">"+data.getName()+"</th><tr>"
			html += "<td>Name of the sport</td><td>Number of the equipment</td></tr><tr>"
			html += "<td></td><td></td></tr><tr>"
			for i in data.select(id):
				html += "<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>"
			html += "</table>"
		except (IndexError, IOError):
			return "Invalid ID"

		return html

	@cherrypy.expose
	def showInstallation(self, id):
		"""
		Exposes the service at localhost:8080/show/[id]/
		"""
		try:
			data.setName("Installation")
			viewB = Template(filename="services/html/header.html")
			viewE = Template(filename="services/html/footer.html")
			html = (viewB.render())
			html += "<h2>Search in the table Installation</h2>"
			html += "<a href=\"javascript:history.go(-1)\">return</a>"
			html += "<table border=1><th colspan=\"5\">"+data.getName()+"</th><tr>"
			html += "<td>Name of the Installation</td><td>Number of the Installation</td><td>Address</td><td>Postal Code</td><td>City</td></tr><tr>"
			html += "<td></td><td></td></tr><tr>"
			for i in data.select(id):
				html += "<td>"+i[0]+"</td><td>"+i[1]+"</td><td>"+i[2]+"</td><td>"+i[3]+"</td><td>"+i[4]+"</td></tr><tr>"
			html += "</table>"
		except (IndexError, IOError):
			return "Invalid ID"

		return html

	@cherrypy.expose
	def showSpecial(self, activity, city):
		"""
		Exposes the service at localhost:8080/show/[id]/
		"""
		try:
			data.setName("Installation")
			viewB = Template(filename="services/html/header.html")
			viewE = Template(filename="services/html/footer.html")
			html = (viewB.render())
			html += "<h2>Search for special activity in a special city</h2>"
			html += "<a href=\"javascript:history.go(-1)\">return</a>"
			html += "<table border=1><th colspan=\"6\">"+data.getName()+"</th><tr>"
			html += "<td>Number of the Installation</td><td>Name of the Installation</td><td>Number of the equipment</td><td>Name of the equipment</td><td>Number of the installation</td><td>Name of the installation</td></tr><tr>"
			html += "<td></td><td></td></tr><tr>"
			for i in data.selectSpecial(activity, city):
				html += "<td>"+i[0]+"</td><td>"+i[1]+"</td><td>"+i[2]+"</td><td>"+i[3]+"</td><td>"+i[4]+"</td></tr><tr>"
			html += "</table>"
		except (IndexError, IOError):
			return "Invalid ID"

		return html

cherrypy.quickstart(WebManager())
