#!/usr/bin/ens python3.4

import codecs
import json

class Activity(object):
	"""docstring for Activity"""
	def __init__(self, ComLib, EquipmentId):
		self.ComLib = ComLib
		self.EquipmentId = EquipmentId

	def __repr__(self):
		return "{} - {}".format(self.ComLib, self.EquipmentId)

	def sql_create(self):
		return "CREATE TABLE IF NOT EXISTS Activity (ComLib text, EquipmentId text)"

	def sql_insert(self):
		return "INSERT INTO Activity VALUES (\"{0}\", \"{1}\")".format(self.ComLib, self.EquipmentId.replace("\"",""))

def parse_json_activity(json_file):
	activity = []
	
	json_data = codecs.open(json_file, encoding="utf-8").read()
	data = json.loads(json_data)

	for item in data["data"]:
		activity.append(Activity(item["ComLib"], item["EquipementId"]))

	return activity
