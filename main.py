#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fiches.installation as ins
import fiches.equipement as eq
import BaseDeDonnees.dataBase as db
items = ins.parse_json_installation("fiches_installations/fichesInstall.json")
items2 = eq.parse_json_equipement("fiches_equipements/data.paysdelaloire.fr.json")
items2csv = eq.parse_csv_equipement("fiches_equipements/equipements.csv")

database = db.DataBase("equipement.db", "equipement", items2csv)
database.table()
database.insert()
liste = database.selectAll()
for row in liste:
	print(row)
database.close()
