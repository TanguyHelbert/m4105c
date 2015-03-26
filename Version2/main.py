#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fiches.Installation as ins
import fiches.Equipment as eq
import fiches.Activity as ac
import BaseDeDonnees.dataBase as db
items = ins.parse_json_installation("data/fichesInstall.json")
items2 = eq.parse_json_equipment("data/data_equipement.json")
items2csv = eq.parse_csv_equipment("data/equipements.csv")
items3 = ac.parse_json_activity("data/data_activites.json")

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