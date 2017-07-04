#!/usr/bin/python3

####################
# Import libraries #
####################

import codecs
import csv
import pdb
import datetime

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

with open(csvFileName) as csvFile, codecs.open(pfad + 'krankheit.csv','wb','utf-8-sig') as krankheitenFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Nachname", "Vorname", "Klasse", "Krankheit"]
    krankheitenFileWriter = csv.DictWriter(krankheitenFile, fieldnames = columnNames, delimiter = ";")
    
    krankheitenFileWriter.writeheader()
    for row in csv.DictReader(csvFile, delimiter = ";"):
        if row["Krankheit"].strip() :
            krankheitenFileWriter.writerow({"Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "Krankheit" : row["Krankheit"], "Klasse" : row["KlasseID"]})
            
##########################
# Write Medikamente file #
##########################

with open(csvFileName) as csvFile, codecs.open(pfad + 'medikamente.csv','wb','utf-8-sig') as medikamenteFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Nachname", "Vorname", "Klasse", "Medikamente"]
    medikamenteFileWriter = csv.DictWriter(medikamenteFile, fieldnames = columnNames, delimiter = ";")
    
    medikamenteFileWriter.writeheader()
    for row in csv.DictReader(csvFile, delimiter = ";"):
        if row["Medikamente"].strip() :
            medikamenteFileWriter.writerow({"Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "Medikamente" : row["Medikamente"], "Klasse" : row["KlasseID"]})

############################
# Write Klassenstufen file #
############################

with open(csvFileName) as csvFile, codecs.open(pfad + 'klassenstufen.csv','wb','utf-8-sig') as klassenstufenFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Klasse", "Anzahl"]
    klassenstufenFileWriter = csv.DictWriter(klassenstufenFile, fieldnames = columnNames, delimiter = ";")

    anzahl = {"5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0, "10" : 0, "11" : 0, "12" : 0}
    klassenstufenFileWriter.writeheader()
    for row in csv.DictReader(csvFile, delimiter = ";"):
        anzahl[row["KlasseID"].strip()] = anzahl[row["KlasseID"].strip()] + 1

    for klasse in range(5,13):
        klassenstufenFileWriter.writerow({ "Klasse" : str(klasse), "Anzahl" : str(anzahl[str(klasse)])})
            
#########################
# Write Geburtstag file #
#########################

# Stupid Hack: In order to not just test for birthdays during the Mathecamp in that particular year I convert everything to 1900 and compare days and months there.

startTimeMathecamp = datetime.date(1900,8,19)
endTimeMathecamp = datetime.date(1900,8,27)

with open(csvFileName) as csvFile, codecs.open(pfad + 'geburtstagskinder.csv','wb','utf-8-sig') as geburtstagskinderFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Nachname", "Vorname", "Klasse", "Geburtstag"]
    geburtstagskinderFileWriter = csv.DictWriter(geburtstagskinderFile, fieldnames = columnNames, delimiter = ";")

    geburtstagskinderFileWriter.writeheader()
    for row in csv.DictReader(csvFile, delimiter = ";"):
        [tag, monat, jahr] = [int(i) for i in row["Geburtstag"].strip().split(".")]
        geburtstag = datetime.date(jahr, monat, tag).replace(year = 1900)
        if geburtstag >= startTimeMathecamp and geburtstag <= endTimeMathecamp:
            geburtstagskinderFileWriter.writerow({ "Klasse" : row["KlasseID"], "Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "Geburtstag" : row["Geburtstag"]})

############################
# Write Themenwünsche file #
############################

with open(csvFileName) as csvFile, codecs.open(pfad + 'themenwuensche.csv','wb','utf-8-sig') as themenwuenscheFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Klasse", "Themenwünsche"]
    themenwuenscheFileWriter = csv.DictWriter(themenwuenscheFile, fieldnames = columnNames, delimiter = ";")

    themenwuensche = {"5" : "", "6" : "", "7" : "", "8" : "", "9" : "", "10" : "", "11" : "", "12" : ""}
    themenwuenscheFileWriter.writeheader()
    for row in csv.DictReader(csvFile, delimiter = ";"):
        wunsch = row["Themenwünsche"]
        if wunsch:
            themenwuensche[row["KlasseID"].strip()] = ", ".join((themenwuensche[row["KlasseID"].strip()], wunsch))

    for klasse in range(5,13):
        themenwuenscheFileWriter.writerow({ "Klasse" : str(klasse), "Themenwünsche" : themenwuensche[str(klasse)][2:] })

##############################
# Write Bereits-bezahlt file #
##############################

###########################
# Write Zimmerwunsch file #
###########################

############################
# Write Emailadressen file #
############################

# Does no parsing or removing double entries at the moment!

emailAdressen = ""

with open(csvFileName) as csvFile, codecs.open(pfad + 'emailAdressen.txt','wb','utf-8-sig') as emailAdressenFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    
    for row in csv.DictReader(csvFile, delimiter = ";"):
        if row["E-Mail Eltern"].strip():
            emailAdressen = emailAdressen + ", " + row["E-Mail Eltern"].strip()
        if row["E-Mail Schüler"].strip():
            emailAdressen = emailAdressen + ", " + row["E-Mail Schüler"].strip()

    emailAdressenFile.write(emailAdressen[2:])
