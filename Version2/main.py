#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import services.fiches.Installation as ins
import services.fiches.Equipment as eq
import services.fiches.Activity as ac
import model.dataBase as db
items = ins.parse_json_installation("services/data/fichesInstall.json")
items2 = eq.parse_json_equipment("services/data/data_equipement.json")
#items2csv = eq.parse_csv_equipment("services/data/equipements.csv")
items3 = ac.parse_json_activity("services/data/data_activites.json")

database = db.DataBase("dataBase.db", "Equipment", items2)
print("Equipment")
database.table()
database.insert()
for row in database.selectAll():
	print(row)
print("Installation")
database.setName("Installation")
database.setItems(items)
database.table()
database.insert()
for row in database.selectAll():
	print(row)
print("Activite")
database.setName("Activity")
database.setItems(items3)
database.table()
database.insert()
for row in database.selectAll():
	print(row)