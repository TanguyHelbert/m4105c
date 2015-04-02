#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# imports of the different services wich will be the table and the file needed to build the data_base
import services.fiches.Installation as ins
import services.fiches.Equipment as eq
import services.fiches.Activity as ac
import model.dataBase as db

# creation of the list containing the data for the tables
items = ins.parse_json_installation("services/data/fichesInstall.json")
items2 = eq.parse_json_equipment("services/data/data_equipement.json")
#items2csv = eq.parse_csv_equipment("services/data/equipements.csv")
items3 = ac.parse_json_activity("services/data/data_activites.json")

# creation of the data_base 
data_base = db.DataBase("database.db", "Installation", items)
# insertion of the data concerning installation in the table installation
print("Installation")
data_base.table()
data_base.insert()
for row in data_base.selectAll():
	print(row)

# insertion of the data concerning installation in the table installation
print("Equipment")
data_base.setName("Equipment")
data_base.setItems(items2)
data_base.table()
data_base.insert()
for row in data_base.selectAll():
	print(row)

# insertion of the data concerning installation in the table installation
print("Activite")
data_base.setName("Activity")
data_base.setItems(items3)
data_base.table()
data_base.insert()
for row in data_base.selectAll():
	print(row)

# unit test 
data_base.setName("Installation")
print(data_base.select("440010002"))
"""
	return : Terrain de Sports	440010002	None	44170	Abbaretz
"""
data_base.setName("Equipment")
print(data_base.select("225442"))
"""
	return : Carrière d'été	225442
"""
data_base.setName("Activity")
print(data_base.select("3501"))
"""
	return : 341 times Gymnastique volontaire	3501
"""