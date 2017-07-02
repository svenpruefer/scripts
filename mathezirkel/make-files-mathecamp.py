#!/usr/bin/python3

####################
# Import libraries #
####################

import codecs
import csv

#######################
# Select file to open #
#######################

csvFileName = input("CSV-Datei zum Einlesen inklusive des relativen Pfades (Standard 1617_Zirkelteilnehmer.csv): ")
if len(csvFileName) < 1:
    csvFileName = "beispiel-tabelle-1.csv"
    
pfad = input("Ort zum Speichern der Output CSV-Dateien (Standard csv/): ")
if len(pfad) < 1:
    pfad = "csv/"

##########################
# Write Anreise Bus file #
##########################

with open(csvFileName) as csvFile, codecs.open(pfad + 'anreise-bus.csv','wb','utf-8-sig') as anreiseBusFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Square", "Nachname", "Vorname", "Notfallnummer 1", "Notfallnummer 2", "Notfallnummer 3"]
    anreiseBusFileWriter = csv.DictWriter(anreiseBusFile, fieldnames = columnNames, delimiter = ";")
    anzahl = 0
    
    anreiseBusFileWriter.writeheader()
    for row in csv.DictReader(csvFile, delimiter = ";"):
        if "Bus" in row["Anreise"]:
            anreiseBusFileWriter.writerow({ "Square" : u"\u25A1 ", "Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "Notfallnummer 1" : row["Notfallnummer 1"], "Notfallnummer 2": row["Notfallnummer 2"], "Notfallnummer 3" : row["Notfallnummer 3"]})
            anzahl = anzahl + 1
        
    anreiseBusFileWriter.writerow({"Square" : "Gesamtzahl:", "Nachname" : str(anzahl)})

#############################
# Write Anreise Privat file #
#############################
    
with open(csvFileName) as csvFile, codecs.open(pfad + 'anreise-privat.csv','wb','utf-8-sig') as anreisePrivatFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Square", "Nachname", "Vorname", "Notfallnummer 1", "Notfallnummer 2", "Notfallnummer 3"]
    anreisePrivatFileWriter = csv.DictWriter(anreisePrivatFile, fieldnames = columnNames, delimiter = ";")
    anzahl = 0
    
    anreisePrivatFileWriter.writeheader()
    for row in csv.DictReader(csvFile, delimiter = ";"):
        if "Privat" in row["Anreise"]:
            anreisePrivatFileWriter.writerow({ "Square" : u"\u25A1 ", "Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "Notfallnummer 1" : row["Notfallnummer 1"], "Notfallnummer 2": row["Notfallnummer 2"], "Notfallnummer 3" : row["Notfallnummer 3"]})
            anzahl = anzahl + 1
        
    anreisePrivatFileWriter.writerow({"Square" : "Gesamtzahl:", "Nachname" : str(anzahl)})
    
##########################
# Write Abreise Bus file #
##########################
    
with open(csvFileName) as csvFile, codecs.open(pfad + 'abreise-bus.csv','wb','utf-8-sig') as abreiseBusFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Square", "Nachname", "Vorname", "Notfallnummer 1", "Notfallnummer 2", "Notfallnummer 3"]
    abreiseBusFileWriter = csv.DictWriter(abreiseBusFile, fieldnames = columnNames, delimiter = ";")
    anzahl = 0
    
    abreiseBusFileWriter.writeheader()
    for row in csv.DictReader(csvFile, delimiter = ";"):
        if "Bus" in row["Abreise"]:
            abreiseBusFileWriter.writerow({ "Square" : u"\u25A1 ", "Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "Notfallnummer 1" : row["Notfallnummer 1"], "Notfallnummer 2": row["Notfallnummer 2"], "Notfallnummer 3" : row["Notfallnummer 3"]})
            anzahl = anzahl + 1
        
    abreiseBusFileWriter.writerow({"Square" : "Gesamtzahl:", "Nachname" : str(anzahl)})
        
#############################
# Write Abreise Privat file #
#############################
    
with open(csvFileName) as csvFile, codecs.open(pfad + 'abreise-privat.csv','wb','utf-8-sig') as abreisePrivatFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Square", "Nachname", "Vorname", "Notfallnummer 1", "Notfallnummer 2", "Notfallnummer 3"]
    abreisePrivatFileWriter = csv.DictWriter(abreisePrivatFile, fieldnames = columnNames, delimiter = ";")
    anzahl = 0
        
    abreisePrivatFileWriter.writeheader()
    for row in csv.DictReader(csvFile, delimiter = ";"):
        if "Privat" in row["Abreise"]:
            abreisePrivatFileWriter.writerow({ "Square" : u"\u25A1 ", "Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "Notfallnummer 1" : row["Notfallnummer 1"], "Notfallnummer 2": row["Notfallnummer 2"], "Notfallnummer 3" : row["Notfallnummer 3"]})
            anzahl = anzahl + 1
        
    abreisePrivatFileWriter.writerow({"Square" : "Gesamtzahl:", "Nachname" : str(anzahl)})
    
########################
# Write Ernährung file #
########################

with open(csvFileName) as csvFile, codecs.open(pfad + 'ernaehrungseinschraenkungen.csv','wb','utf-8-sig') as ernaehrungFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Nachname", "Vorname", "Ernährung"]
    ernaehrungFileWriter = csv.DictWriter(ernaehrungFile, fieldnames = columnNames, delimiter = ";")
    
    ernaehrungFileWriter.writeheader()
    for row in csv.DictReader(csvFile, delimiter = ";"):
        if row["Ernährung"].strip():
            ernaehrungFileWriter.writerow({"Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "Ernährung" : row["Ernährung"]})
            
###############################
# Write Fahrgemeinschaft file #
###############################

with open(csvFileName) as csvFile, codecs.open(pfad + 'fahrgemeinschaft.csv','wb','utf-8-sig') as fahrgemeinschaftFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Nachname", "Vorname", "PLZ", "Ort", "E-Mail Eltern", "E-Mail Schüler"]
    fahrgemeinschaftFileWriter = csv.DictWriter(fahrgemeinschaftFile, fieldnames = columnNames, delimiter = ";")
    
    fahrgemeinschaftFileWriter.writeheader()
    for row in csv.DictReader(csvFile, delimiter = ";"):
        if row["Fahrgemeinschaft"] == "WAHR":
            fahrgemeinschaftFileWriter.writerow({"Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "PLZ" : row["PLZ"], "Ort" : row["Ort"], "E-Mail Eltern" : row["E-Mail Eltern"], "E-Mail Schüler" : row["E-Mail Schüler"]})
            
##########################
# Write Instrumente file #
##########################

with open(csvFileName) as csvFile, codecs.open(pfad + 'instrumente.csv','wb','utf-8-sig') as instrumenteFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Nachname", "Vorname", "Instrument", "E-Mail Eltern", "E-Mail Schüler"]
    instrumenteFileWriter = csv.DictWriter(instrumenteFile, fieldnames = columnNames, delimiter = ";")
    
    instrumenteFileWriter.writeheader()
    for row in csv.DictReader(csvFile, delimiter = ";"):
        if row["Instrument"].strip() :
            instrumenteFileWriter.writerow({"Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "Instrument" : row["Instrument"], "E-Mail Eltern" : row["E-Mail Eltern"], "E-Mail Schüler" : row["E-Mail Schüler"]})
            
##########################
# Write Krankheiten file #
##########################

##########################
# Write Medikamente file #
##########################

#########################
# Write Geburtstag file #
#########################

############################
# Write Themenwünsche file #
############################

##############################
# Write Bereits-bezahlt file #
##############################

###########################
# Write Zimmerwunsch file #
###########################

############################
# Write Emailadressen file #
############################
