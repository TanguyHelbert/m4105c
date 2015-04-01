#!/usr/bin/ens python3.4

"""
numero : InsNumeroInstall
nom : InsNom
adresse : InsNoVoie
code_postal : InsCodePostal
ville : ComLib
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

	def __repr__(self):
		return "{} - {}".format(self.num, self.name, self.address, self.postalCode, self.city)

	def sql_create(self):
		return "CREATE TABLE IF NOT EXISTS Installation (name text, numb text, address text, postalCode text, city text)"

	def sql_insert(self):
		return "INSERT INTO Installation VALUES (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\")".format(self.name, self.numb, self.address, self.postalCode, self.city)


def parse_json_installation(json_file):
	installation = []
	
	json_data = codecs.open(json_file, encoding="utf-8").read()
	data = json.loads(json_data)

	for item in data["data"]:
		installation.append(Installation(item["geo"]["name"], item["InsNumeroInstall"], item["InsNoVoie"], item["InsCodePostal"], item["ComLib"]))

	return installation

def parse_csv_installation(csv_file):
	installation = []

	with open(csv_file, 'rt') as csvfile:
		installationReader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in installationReader:
			installation.append(Installation(row[3], row[2]))

	return installation
