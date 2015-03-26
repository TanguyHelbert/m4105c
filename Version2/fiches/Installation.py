#!/usr/bin/ens python3.4

import codecs
import json
import csv

class Installation:
	"""docstring for Installation"""
	def __init__(self, name, numb):
		self.name = name
		self.numb = numb

	def __repr__(self):
		return "{} - {}".format(self.num, self.name)

	def sql_create(self):
		return "CREATE TABLE IF NOT EXISTS Installation (name text, numb text)"

	def sql_insert(self):
		return "INSERT INTO Installation VALUES (\"{0}\", \"{1}\")".format(self.name, self.numb)


def parse_json_installation(json_file):
	installation = []
	
	json_data = codecs.open(json_file, encoding="utf-8").read()
	data = json.loads(json_data)

	for item in data["data"]:
		installation.append(Installation(item["ComLib"], item["InsNumeroInstall"]))

	return installation

def parse_csv_installation(csv_file):
	installation = []

	with open(csv_file, 'rt') as csvfile:
		installationReader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in installationReader:
			installation.append(Installation(row[3], row[2]))

	return installation
