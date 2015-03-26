# heure de passage 10h50
# C0/04 C0/05

import cherrypy
import BaseDeDonnees.dataBase as db

#localhost:8080
#localhost:8080/show_all

#data = json.loads(open("fiches_Equipments/data.paysdelaloire.fr.json").read())

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
		html = "<h1>Sports facilities of countries of the Loire</h1>"
		html += "<a href=show_allEquipment>table Equipment</a></br>"
		html += "<a href=show_allActivity>table Activity</a></br>"
		html += "<a href=show_allInstallation>table Installation</a></br>"
		html += "<form action=\"showEquipment\">"
		html += "search in Equipment : <input type=\"text\" name=\"id\">"
		html += "<input type=\"submit\">"
		html += "</form>"
		html += "<form action=\"showActivity\">"
		html += "search in Activity : <input type=\"text\" name=\"id\">"
		html += "<input type=\"submit\">"
		html += "</form>"
		html += "<form action=\"showInstallation\">"
		html += "search in Installation: <input type=\"text\" name=\"id\">"
		html += "<input type=\"submit\">"
		html += "</form>"
		return html

	@cherrypy.expose
	def show_allEquipment(self):
		"""
		Exposes the service at localhost:8080/show_all/
		"""
		data.setName("Equipment")
		l = []
		l.append('<h1>Sports facilities of countries of the Loire</h1>')
		l.append('<h2>List of all elements in the table '+data.getName()+'</h2>')
		l.append("<a href=\"index\">retour accueil</a>")
		l.append('<table border=1><th colspan="2">'+data.getName()+'</th><tr>')
		l.append("<td>Equipment Name</td><td>Ins Num</td></tr><tr>")
		l.append('<td></td><td></td></tr><tr>')
		for i in data.selectAll():
			l.append("<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>")
		l.append("</table>")
		return (" ".join(l))

	@cherrypy.expose
	def show_allActivity(self):
		"""
		Exposes the service at localhost:8080/show_all/
		"""
		data.setName("Activity")
		l = []
		l.append('<h1>Sports facilities of countries of the Loire</h1>')
		l.append('<h2>List of all elements in the table '+data.getName()+'</h2>')
		l.append("<a href=\"index\">retour accueil</a>")
		l.append('<table border=1><th colspan="2">'+data.getName()+'</th><tr>')
		l.append("<td>ComLib</td><td>EquipmentId</td></tr><tr>")
		l.append('<td></td><td></td></tr><tr>')
		for i in data.selectAll():
		    l.append("<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>")
		l.append("</table>")
		return (" ".join(l))

	@cherrypy.expose
	def show_allInstallation(self):
		"""
		Exposes the service at localhost:8080/show_all/
		"""
		data.setName("Installation")
		l = []
		l.append('<h1>Sports facilities of countries of the Loire</h1>')
		l.append('<h2>List of all elements in the table '+data.getName()+'</h2>')
		l.append("<a href=\"index\">retour accueil</a>")
		l.append('<table border=1><th colspan="2">'+data.getName()+'</th><tr>')
		l.append("<td>name</td><td>numb</td></tr><tr>")
		l.append('<td></td><td></td></tr><tr>')
		for i in data.selectAll():
		    l.append("<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>")
		l.append("</table>")
		return (" ".join(l))

	@cherrypy.expose
	def showEquipment(self, id):
		"""
		Exposes the service at localhost:8080/show/[id]/
		"""
		try:
			data.setName("Equipment")
			l = []
			l.append('<h1>Sports facilities of countries of the Loire</h1>')
			l.append('<h2>Search in the table Equipment</h2>')
			l.append("<a href=\"index\">retour accueil</a>")
			l.append('<table border=1><th colspan="2">'+data.getName()+'</th><tr>')
			for i in data.select(id):
				l.append("<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>")
			l.append("</table>")
		except (IndexError, IOError):
			return "Invalid ID"

		return (" ".join(l))

	@cherrypy.expose
	def showActivity(self, id):
		"""
		Exposes the service at localhost:8080/show/[id]/
		"""
		try:
			data.setName("Activity")
			l = []
			l.append('<h1>Sports facilities of countries of the Loire</h1>')
			l.append('<h2>Search in the table Activity</h2>')
			l.append("<a href=\"index\">retour accueil</a>")
			l.append('<table border=1><th colspan="2">'+data.getName()+'</th><tr>')
			for i in data.select(id):
				l.append("<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>")
			l.append("</table>")
		except (IndexError, IOError):
			return "Invalid ID"

		return (" ".join(l))

	@cherrypy.expose
	def showInstallation(self, id):
		"""
		Exposes the service at localhost:8080/show/[id]/
		"""
		try:
			data.setName("Installation")
			l = []
			l.append('<h1>Sports facilities of countries of the Loire</h1>')
			l.append('<h2>Search in the table Installation</h2>')
			l.append("<a href=\"index\">retour accueil</a>")
			l.append('<table border=1><th colspan="2">'+data.getName()+'</th><tr>')
			for i in data.select(id):
				l.append("<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>")
			l.append("</table>")
		except (IndexError, IOError):
			return "Invalid ID"

		return (" ".join(l))

cherrypy.quickstart(WebManager())
