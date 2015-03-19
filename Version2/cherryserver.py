import cherrypy
import BaseDeDonnees.dataBase as db

#localhost:8080
#localhost:8080/show_all

#data = json.loads(open("fiches_equipements/data.paysdelaloire.fr.json").read())

liste_fake = []
data = db.DataBase("equipement.db", "equipement", liste_fake)

class WebManager(object):
    """
    Exposes web services
    """
    @cherrypy.expose
    def index(self):
        """
        Exposes the service at localhost:8080/
        """
        return "There are {0} items".format(data.countAttribut())

    @cherrypy.expose
    def show_all(self):
        """
        Exposes the service at localhost:8080/show_all/
        """
        l = []
        l.append("<table border=1><tr>")
        for i in data.selectAll():
            l.append("<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>")
        l.append("</table>")
        return (" ".join(l))

    @cherrypy.expose
    def show(self, attribut, cible):
        """
        Exposes the service at localhost:8080/show/[id]/
        """
        try:
            item = "<p>"+str(data.select(attribut, cible))+"</p>"
        except (IndexError, IOError):
            return "Invalid ID"

        return item


cherrypy.quickstart(WebManager())
