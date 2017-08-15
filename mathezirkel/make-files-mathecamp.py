#!/usr/bin/python3

####################
# Import libraries #
####################

import codecs
import csv
import pdb
import datetime
import networkx as nx

#######################
# Select file to open #
#######################

csvFileName = input("CSV-Datei zum Einlesen inklusive des relativen Pfades (Standard ../1617_camp.csv): ")
if len(csvFileName) < 1:
    csvFileName = "../1617_camp.csv"
    
pfad = input("Ort zum Speichern der Output CSV-Dateien (Standard ../csv/): ")
if len(pfad) < 1:
    pfad = "../csv/"

##########################
# Write Anreise Bus file #
##########################

with open(csvFileName) as csvFile, codecs.open(pfad + 'anreise-bus.csv','wb','utf-8-sig') as anreiseBusFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Square", "Nachname", "Vorname", "Notfallnummer 1", "Notfallnummer 2", "Notfallnummer 3"]
    anreiseBusFileWriter = csv.DictWriter(anreiseBusFile, fieldnames = columnNames, delimiter = ";")
    anzahl = 0
    
    anreiseBusFileWriter.writeheader()
    for row in csvFileReader:
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
    for row in csvFileReader:
        if row["Anreise"].startswith("Privat") or row["Anreise"].startswith("Selbst") or row["Anreise"].startswith("Auto"):
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
    for row in csvFileReader:
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
    for row in csvFileReader:
        if row["Abreise"].startswith("Privat") or row["Abreise"].startswith("Selbst") or row["Abreise"].startswith("Auto"):
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
    for row in csvFileReader:
        if row["Ernährung"].strip():
            ernaehrungFileWriter.writerow({"Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "Ernährung" : row["Ernährung"]})
            
###############################
# Write Fahrgemeinschaft file #
###############################

with open(csvFileName) as csvFile, codecs.open(pfad + 'fahrgemeinschaft.csv','wb','utf-8-sig') as fahrgemeinschaftFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Nachname", "Vorname", "PLZ", "Ort", "E-Mail Eltern", "Festnetz"]
    fahrgemeinschaftFileWriter = csv.DictWriter(fahrgemeinschaftFile, fieldnames = columnNames, delimiter = ";")
    
    fahrgemeinschaftFileWriter.writeheader()
    for row in csvFileReader:
        if row["Fahrgemeinschaft"] == "TRUE":
            fahrgemeinschaftFileWriter.writerow({"Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "PLZ" : row["PLZ"], "Ort" : row["Ort"], "E-Mail Eltern" : row["E-Mail Eltern"], "Festnetz" : row["Festnetz"]})
            
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
    for row in csvFileReader:
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
    for row in csvFileReader:
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
    for row in csvFileReader:
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
    for row in csvFileReader:
        [tag, monat, jahr] = [int(i) for i in row["Geburtstag"].strip().split(".")]
        #pdb.set_trace()
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
    for row in csvFileReader:
        wunsch = row["Themenwünsche"]
        if wunsch:
            themenwuensche[row["KlasseID"].strip()] = ", ".join((themenwuensche[row["KlasseID"].strip()], wunsch))

    for klasse in range(5,13):
        themenwuenscheFileWriter.writerow({ "Klasse" : str(klasse), "Themenwünsche" : themenwuensche[str(klasse)][2:] })

##############################
# Write Bereits-bezahlt file #
##############################

with open(csvFileName) as csvFile, codecs.open(pfad + 'bereits-bezahlt.csv','wb','utf-8-sig') as bereitsBezahltFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Nachname", "Vorname", "Zu Bezahlen", "Bereits Bezahlt", "Differenz"]
    bereitsBezahltFileWriter = csv.DictWriter(bereitsBezahltFile, fieldnames = columnNames, delimiter = ";")

    bereitsBezahltFileWriter.writeheader()
    for row in csvFileReader:
        if row["Bezahlter Betrag"].strip():
            bezahlt = int(row["Bezahlter Betrag"])
        else:
            bezahlt = 0

        if row["Camppreis"].strip():
            camppreis = int(row["Camppreis"])
        else:
            camppreis = 0

        differenz = bezahlt - camppreis
        bereitsBezahltFileWriter.writerow({"Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "Zu Bezahlen" : row["Camppreis"], "Bereits Bezahlt" : row["Bezahlter Betrag"], "Differenz" : str(differenz)})
    
###########################
# Write Zimmerwunsch file #
###########################

adjacencyDictionnary = {}

with open(csvFileName) as csvFile, codecs.open(pfad + 'zimmerwunsch.txt','wb','utf-8-sig') as zimmerwunschFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")

    for row in csvFileReader:
        listeFreunde = row["Freunde"].strip().split(",")
        adjacencyDictionnary[row["Vorname"] + " " + row["Nachname"]] = [freund.strip() for freund in listeFreunde if freund.strip() != ""]

    #pdb.set_trace()
    
    freundeGraph = nx.from_dict_of_lists(adjacencyDictionnary)
    freundesGruppen = nx.connected_components(freundeGraph)

    for gruppe in freundesGruppen:
        if len(gruppe) > 1:
            zimmerwunschFile.write(str(gruppe) + "\n")

############################
# Write Emailadressen file #
############################

# Does no parsing or removing double entries at the moment!

emailAdressen = ""

with open(csvFileName) as csvFile, codecs.open(pfad + 'emailAdressen.txt','wb','utf-8-sig') as emailAdressenFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    
    for row in csvFileReader:
        if row["E-Mail Eltern"].strip():
            emailAdressen = emailAdressen + ", " + row["E-Mail Eltern"].strip()
        if row["E-Mail Schüler"].strip():
            emailAdressen = emailAdressen + ", " + row["E-Mail Schüler"].strip()

    emailAdressenFile.write(emailAdressen[2:])

###########################
# Write Versicherung file #
###########################

with open(csvFileName) as csvFile, codecs.open(pfad + 'versicherung.csv','wb','utf-8-sig') as versicherungFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    columnNames = ["Nachname", "Vorname", "Geburtsdatum", "Betreuer"]
    versicherungFileWriter = csv.DictWriter(versicherungFile, fieldnames = columnNames, delimiter = ";")
    versicherungFileWriter.writeheader()
    
    for row in csvFileReader:
        versicherungFileWriter.writerow({"Nachname" : row["Nachname"], "Vorname" : row["Vorname"], "Geburtsdatum" : row["Geburtstag"], "Betreuer" : "Nein"})


####################################
# Write Zirkelzusammenfassung file #
####################################

##########################################
# Print Geschlechterverteilung on Screen #
##########################################

maennlich = 0
weiblich = 0
with open(csvFileName) as csvFile:
    csvFileReader = csv.DictReader(csvFile, delimiter = ";")
    
    for row in csvFileReader:
        if row["Geschlecht"] == "m":
            maennlich = maennlich + 1
        elif row["Geschlecht"] == "w":
            weiblich = weiblich + 1
        else:
            print("Unklares Geschlecht entdeckt.")

print("Männliche Teilnehmer: " + str(maennlich) + "\n")
print("Weibliche Teilnehmerinnen: " + str(weiblich) + "\n")

