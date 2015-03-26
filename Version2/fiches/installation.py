#!/usr/bin/ens python3.4

import codecs
import json
import csv

class Installation:
	"""docstring for Installation"""
	def __init__(self, nom, num):
		self.nom = nom
		self.num = num

	def __repr__(self):
		return "{} - {}".format(self.num, self.nom)

	def sql_create(self):
		return "CREATE TABLE IF NOT EXISTS installation (numero text, nom text)"

	def sql_insert(self):
		return "INSERT INTO installation VALUES (\"{1}\", \"{0}\")".format(self.nom, self.num)


def parse_json_installation(json_file):
	installations = []
	
	json_data = codecs.open(json_file, encoding="utf-8").read()
	data = json.loads(json_data)

	for item in data["data"]:
		installations.append(Installation(item["ComLib"], item["InsNumeroInstall"]))

	return installations

def parse_csv_installation(csv_file):
	installation = []

	with open(csv_file, 'rt') as csvfile:
		equipementReader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in equipementReader:
			equipement.append(Installation(row[3], row[2]))

	return installation
