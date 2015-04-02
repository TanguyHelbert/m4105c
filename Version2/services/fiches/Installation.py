#!/usr/bin/ens python3.4

"""
name : InsNom
numb : InsNumeroInstall
address : InsNoVoie
postalCode : InsCodePostal
city : ComLib
"""

import codecs
import json
import csv

class Installation:
	"""docstring for Installation"""
	def __init__(self, name, numb, address, postalCode, city):
		self.name = name
		self.numb = numb
		self.address = address
		self.postalCode = postalCode
		self.city = city

	"""return the reprsentation of the object when called raw"""
	def __repr__(self):
		return "{} - {} - {} - {} - {}".format(self.num, self.name, self.address, self.postalCode, self.city)

	"""return the sql request to create the table"""
	def sql_create(self):
		return "CREATE TABLE IF NOT EXISTS Installation (name text, numb text, address text, postalCode text, city text)"

	"""return the sql request to insert into the table"""
	def sql_insert(self):
		return "INSERT INTO Installation VALUES (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\")".format(self.name, self.numb, self.address, self.postalCode, self.city)

"""create the list of json data"""
def parse_json_installation(json_file):
	installation = [] # empty list
	
	json_data = codecs.open(json_file, encoding="utf-8").read() # take all items in format json
	data = json.loads(json_data) # take the json data and make it into a list attribute:value

	for item in data["data"]:
		installation.append(Installation(item["geo"]["name"], item["InsNumeroInstall"], item["InsNoVoie"], item["InsCodePostal"], item["ComLib"]))

	return installation

"""create the list of csv data"""
def parse_csv_installation(csv_file):
	installation = [] # empty list

	with open(csv_file, 'rt') as csvfile: # open the csv file
		installationReader = csv.reader(csvfile, delimiter=',', quotechar='"') # take the csv data and make it into a list
		for row in installationReader:
			installation.append(Installation(row[3], row[2]))

	return installation
