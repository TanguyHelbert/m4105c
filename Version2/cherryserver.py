#nomville
#nomactivite

# heure de passage 10h50
# C0/04 C0/05

import cherrypy
import model.dataBase as db
from mako.template import Template

#localhost:8080
#localhost:8080/show_all

list_fake = [] # empty list to build the database already existing
data = db.DataBase("dataBase.db", "Equipment", list_fake)

class WebManager(object):
	"""
	Exposes web services
	"""
	@cherrypy.expose
	def index(self):
		"""
		Exposes the service at localhost:8080/
		"""
		view_B = Template(filename="services/html/header.html")
		view_E = Template(filename="services/html/footer.html")
		view_I1 = Template(filename="services/html/firstView.html")
		html = (view_B.render())
		html += (view_I1.render())
		html += (view_E.render())
		return html

	@cherrypy.expose
	def show_allInstallation(self):
		"""
		Exposes the service at localhost:8080/show_allInstallation/
		"""
		data.setName("Installation")
		view_B = Template(filename="services/html/header.html")
		view_E = Template(filename="services/html/footer.html")
		html = (view_B.render())
		html += "<h2>List of all elements in the table "+data.getName()+"</h2>"
		html += "<a href=\"javascript:history.go(-1)\">return</a>"
		html += "<table border=1><th colspan=\"5\" id=\"grosTitre\">"+data.getName()+"</th><tr>"
		html += "<th>Name of the Installation</th><th>Number of the Installation</th><th>Address</th><th>Postal Code</th><th>City</th></tr><tr>"
		html += "<td></td><td></td></tr><tr>"
		for i in data.selectAll():
			html += "<td>"+i[0]+"</td><td>"+i[1]+"</td><td>"+i[2]+"</td><td>"+i[3]+"</td><td>"+i[4]+"</td></tr><tr>"
		html += "</table>"
		html += (view_E.render())
		return html

	@cherrypy.expose
	def show_allEquipment(self):
		"""
		Exposes the service at localhost:8080/show_allEquipment/
		"""
		data.setName("Equipment")
		view_B = Template(filename="services/html/header.html")
		view_E = Template(filename="services/html/footer.html")
		html = (view_B.render())
		html += "<h2>List of all elements in the table "+data.getName()+"</h2>"
		html += "<a href=\"javascript:history.go(-1)\">return</a>"
		html += "<table border=1><th colspan=\"2\" id=\"grosTitre\">"+data.getName()+"</th><tr>"
		html += "<th>Name of the equipment</th><th>Number of the equipment</th></tr><tr>"
		html += "<td></td><td></td></tr><tr>"
		for i in data.selectAll():
			html += "<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>"
		html += "</table>"
		html += (view_E.render())
		return html

	@cherrypy.expose
	def show_allActivity(self):
		"""
		Exposes the service at localhost:8080/show_allActivity/
		"""
		data.setName("Activity")
		view_B = Template(filename="services/html/header.html")
		view_E = Template(filename="services/html/footer.html")
		html = (view_B.render())
		html += "<h2>List of all elements in the table "+data.getName()+"</h2>"
		html += "<a href=\"javascript:history.go(-1)\">return</a>"
		html += "<table border=1><th colspan=\"2\" id=\"grosTitre\">"+data.getName()+"</th><tr>"
		html += "<th>Name of the sport</th><th>Number of the activity code</th></tr><tr>"
		html += "<td></td><td></td></tr><tr>"
		for i in data.selectAll():
			html += "<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>"
		html += "</table>"
		html += (view_E.render())
		return html

	@cherrypy.expose
	def showInstallation(self, id):
		"""
		Exposes the service at localhost:8080/showInstallation/[id]/
		"""
		try:
			data.setName("Installation")
			view_B = Template(filename="services/html/header.html")
			view_E = Template(filename="services/html/footer.html")
			html = (view_B.render())
			html += "<h2>Search in the table Installation</h2>"
			html += "<a href=\"javascript:history.go(-1)\">return</a>"
			html += "<table border=1><th colspan=\"5\" id=\"grosTitre\">"+data.getName()+"</th><tr>"
			html += "<th>Name of the Installation</th><th>Number of the Installation</th><th>Address</th><th>Postal Code</th><th>City</th></tr><tr>"
			html += "<td></td><td></td></tr><tr>"
			for i in data.select(id):
				html += "<td>"+i[0]+"</td><td>"+i[1]+"</td><td>"+i[2]+"</td><td>"+i[3]+"</td><td>"+i[4]+"</td></tr><tr>"
			html += "</table>"
		except (IndexError, IOError):
			return "Invalid ID"

		return html

	@cherrypy.expose
	def showEquipment(self, id):
		"""
		Exposes the service at localhost:8080/showEquipment/[id]/
		"""
		try:
			data.setName("Equipment")
			view_B = Template(filename="services/html/header.html")
			view_E = Template(filename="services/html/footer.html")
			html = (view_B.render())
			html += "<h2>Search in the table Equipment</h2>"
			html += "<a href=\"javascript:history.go(-1)\">return</a>"
			html += "<table border=1><th colspan=\"2\" id=\"grosTitre\">"+data.getName()+"</th><tr>"
			html += "<th>Name of the equipment</th><th>Number of the equipment</th></tr><tr>"
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
		Exposes the service at localhost:8080/showActivity/[id]/
		"""
		try:
			data.setName("Activity")
			view_B = Template(filename="services/html/header.html")
			view_E = Template(filename="services/html/footer.html")
			html = (view_B.render())
			html += "<h2>Search in the table Activity</h2>"
			html += "<a href=\"javascript:history.go(-1)\">return</a>"
			html += "<table border=1><th colspan=\"2\" id=\"grosTitre\">"+data.getName()+"</th><tr>"
			html += "<th>Name of the sport</th><th>Number of the equipment</th></tr><tr>"
			html += "<td></td><td></td></tr><tr>"
			for i in data.select(id):
				html += "<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>"
			html += "</table>"
		except (IndexError, IOError):
			return "Invalid ID"

		return html

	@cherrypy.expose
	def showSpecial(self, activity, city):
		"""
		Exposes the service at localhost:8080/showSpecial/[activity]/[city]
		"""
		try:
			data.setName("Installation")
			view_B = Template(filename="services/html/header.html")
			view_E = Template(filename="services/html/footer.html")
			html = (view_B.render())
			html += "<h2>Search for special activity in a special city</h2>"
			html += "<a href=\"javascript:history.go(-1)\">return</a>"
			html += "<table border=1><th colspan=\"6\" id=\"grosTitre\">"+data.getName()+"</th><tr>"
			html += "<th>Number of the Installation</th><th>Name of the Installation</th><th>Number of the equipment</th><th>Name of the equipment</th><th>Number of the installation</th><th>Name of the installation</th></tr><tr>"
			html += "<td></td><td></td></tr><tr>"
			for i in data.selectSpecial(activity, city):
				html += "<td>"+i[0]+"</td><td>"+i[1]+"</td><td>"+i[2]+"</td><td>"+i[3]+"</td><td>"+i[4]+"</td></tr><tr>"
			html += "</table>"
		except (IndexError, IOError):
			return "Invalid ID"

		return html

cherrypy.quickstart(WebManager())
