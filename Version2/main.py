#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fiches.installation as ins
import fiches.equipement as eq
import fiches.activites as ac
import BaseDeDonnees.dataBase as db
items = ins.parse_json_installation("data/fichesInstall.json")
items2 = eq.parse_json_equipement("data/data_equipement.json")
items2csv = eq.parse_csv_equipement("data/equipements.csv")
items3 = ac.parse_json_activites("data/data_activites.json")

database = db.DataBase("dataBase.db", "equipement", items2)
print("equipement")
database.table()
database.insert()
for row in database.selectAll():
	print(row)
print("installation")
database.setName("installation")
database.setItems(items)
database.table()
database.insert()
for row in database.selectAll():
	print(row)
print("activites")
database.setName("activites")
database.setItems(items3)
database.table()
database.insert()
for row in database.selectAll():
	print(row)