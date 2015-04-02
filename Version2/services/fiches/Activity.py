#!/usr/bin/ens python3.4

"""
name : ComLib
numb : ActCode
numb : EquipmentId
"""

import codecs
import json

class Activity(object):
	"""docstring for Activity"""
	def __init__(self, name, numb, numb2):
		self.name = name
		self.numb = numb
		self.numb2 = numb2

	"""return the reprsentation of the object when called raw"""
	def __repr__(self):
		return "{} - {} - {}".format(self.name, self.numb, self.numb2)

	"""return the sql request to create the table"""
	def sql_create(self):
		return "CREATE TABLE IF NOT EXISTS Activity (name text, numb text, numb2 text)"

	"""return the sql request to insert into the table"""
	def sql_insert(self):
		return "INSERT INTO Activity VALUES (\"{0}\", \"{1}\", \"{2}\")".format(self.name, self.numb, self.numb2)

"""create the list of json data"""
def parse_json_activity(json_file):
	activity = [] # empty file
	
	json_data = codecs.open(json_file, encoding="utf-8").read() # take all items in format json
	data = json.loads(json_data) # take the json data and make it into a list attribute:value

	for item in data["data"]:
		activity.append(Activity(item["ActLib"], item["ActCode"], item["EquipementId"]))

	return activity
