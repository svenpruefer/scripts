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

#############
# Read file #
#############

with open(csvFileName) as csvFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    
    ##########################
    # Write Anreise Bus file #
    ##########################
    
    with codecs.open(pfad + 'anreise-bus.csv','wb','utf-8-sig') as anreiseBusFile:
        columnNames = ["Square", "Nachname", "Vorname", "Notfallnummer 1", "Notfallnummer 2", "Notfallnummer 3"]
        anreiseBusFileWriter = csv.DictWriter(anreiseBusFile, fieldnames = columnNames, delimiter = ";")
        anzahl = 0
        
        anreiseBusFileWriter.writeheader()
        for row in csvFileReader:
            if row["Anreise"] == "Bus":
                anreiseBusFileWriter.writerow({ "Square" : u"\u25A1 ", "Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "Notfallnummer 1" : row["Notfallnummer 1"], "Notfallnummer 2": row["Notfallnummer 2"], "Notfallnummer 3" : row["Notfallnummer 3"]})
                anzahl = anzahl + 1
        
        anreiseBusFileWriter.writerow({"Square" : "Gesamtzahl:", "Nachname" : str(anzahl)})
        
    #############################
    # Write Anreise Privat file #
    #############################
    
    with codecs.open(pfad + 'anreise-privat.csv','wb','utf-8-sig') as anreisePrivatFile:
        columnNames = ["Square", "Nachname", "Vorname", "Notfallnummer 1", "Notfallnummer 2", "Notfallnummer 3"]
        anreisePrivatFileWriter = csv.DictWriter(anreisePrivatFile, fieldnames = columnNames, delimiter = ";")
        anzahl = 0
        
        anreisePrivatFileWriter.writeheader()
        for row in csvFileReader:
            if  "Privat" in row["Anreise"]:
                anreisePrivatFileWriter.writerow({ "Square" : u"\u25A1 ", "Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "Notfallnummer 1" : row["Notfallnummer 1"], "Notfallnummer 2": row["Notfallnummer 2"], "Notfallnummer 3" : row["Notfallnummer 3"]})
                anzahl = anzahl + 1
        
        anreisePrivatFileWriter.writerow({"Square" : "Gesamtzahl:", "Nachname" : str(anzahl)})
        
        
    
    
