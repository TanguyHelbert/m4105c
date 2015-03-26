import cherrypy
import BaseDeDonnees.dataBase as db

#localhost:8080
#localhost:8080/show_all

#data = json.loads(open("fiches_equipements/data.paysdelaloire.fr.json").read())

liste_fake = []
data = db.DataBase("dataBase.db", "equipement", liste_fake)

class WebManager(object):
    """
    Exposes web services
    """
    @cherrypy.expose
    def index(self):
        """
        Exposes the service at localhost:8080/
        """
        html = "<a href=show_all/equipement>table equipement</a></br>"
        html += "<a href=show_all/activites>table activites</a></br>"
        html += "<a href=show_all/installation>table installation</a></br>"
        html += "<form action=\"show\">"
        html += "<input type=\"text\" name=\"table\"></br>"
        html += "<input type=\"text\" name=\"id\">"
        html += "<input type=\"submit\">"
        html += "</form>"
        return html
        #return "There are {0} items".format(data.countAttribut())

    @cherrypy.expose
    def show_all(self,table):
        """
        Exposes the service at localhost:8080/show_all/
        """
        data.setName(table)
        l = []
        l.append('<table border=1><th colspan="2">'+data.getName()+'</th><tr>')
        for i in data.selectAll():
            l.append("<td>"+i[0]+"</td><td>"+i[1]+"</td></tr><tr>")
        l.append("</table>")
        return (" ".join(l))

    @cherrypy.expose
    def show(self, table, id):
        """
        Exposes the service at localhost:8080/show/[id]/
        """
        try:
            data.setName(table)
            item = "<h1>"+data.getName()+"</h1><p>"+str(data.select(id))+"</p>"
        except (IndexError, IOError):
            return "Invalid ID"

        return item


cherrypy.quickstart(WebManager())
