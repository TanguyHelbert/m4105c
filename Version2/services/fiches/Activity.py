#!/usr/bin/ens python3.4

"""
numero : EquipmentId
nom : ComLib
"""

import codecs
import json

class Activity(object):
	"""docstring for Activity"""
	def __init__(self, name, numb, numb2):
		self.name = name
		self.numb = numb
		self.numb2 = numb2

	def __repr__(self):
		return "{} - {}".format(self.name, self.EquipmentId)

	def sql_create(self):
		return "CREATE TABLE IF NOT EXISTS Activity (name text, numb text, numb2 text)"

	def sql_insert(self):
		return "INSERT INTO Activity VALUES (\"{0}\", \"{1}\", \"{2}\")".format(self.name, self.numb, self.numb2)

def parse_json_activity(json_file):
	activity = []
	
	json_data = codecs.open(json_file, encoding="utf-8").read()
	data = json.loads(json_data)

	for item in data["data"]:
		activity.append(Activity(item["ActLib"], item["ActCode"], item["EquipementId"]))

	return activity
