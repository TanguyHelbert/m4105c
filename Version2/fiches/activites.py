#!/usr/bin/ens python3.4

import codecs
import json

class Activites(object):
	"""docstring for Activites"""
	def __init__(self, ComLib, EquipementId):
		self.ComLib = ComLib
		self.EquipementId = EquipementId

	def __repr__(self):
		return "{} - {}".format(self.ComLib, self.EquipementId)

	def sql_create(self):
		return "CREATE TABLE IF NOT EXISTS activites (ComLib text, EquipementId text)"

	def sql_insert(self):
		return "INSERT INTO activites VALUES (\"{1}\", \"{0}\")".format(self.ComLib, self.EquipementId.replace("\"",""))

def parse_json_activites(json_file):
	activites = []
	
	json_data = codecs.open(json_file, encoding="utf-8").read()
	data = json.loads(json_data)

	for item in data["data"]:
		activites.append(Activites(item["ComLib"], item["EquipementId"]))

	return activites
