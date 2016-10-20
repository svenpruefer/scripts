#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs

# Definiere Titelfelder, die für Serienbrief gebraucht werden
serienbrief_titel_reihenfolge = ["ZirkelID","Vorname","Nachname","Geschlecht","KlasseID","Straße","PLZ","Ort"]
serienbrief_titel = dict(zip(serienbrief_titel_reihenfolge,[0 for x in range(len(serienbrief_titel_reihenfolge))]))

# Oeffne Tabelle, die per Bericht aus Base exportiert wird. Sie darf als Zwischenzeilen nur solche mit Beginn "ZirkelID" haben.
name = raw_input("CSV-Datei zum Einlesen inklusive des relativen Pfades: ")
if len(name) < 1 : name = "1617_Zirkelteilnehmer.csv"

# Erfrage Optionen für Serienbrieffunktion oder alle Daten sowie Output-Pfad. Typüberprüfung von option?
pfad = raw_input("Ort zum Speichern der CSV-Dateien (Standard csv/): ")
if len(pfad) < 1 : pfad = "csv/"
option = raw_input("Wähle eine der folgenden Ausgabeoptionen (Standard 1):\n[1] Volle Ausgabe\n[2] Serienbriefausgabe\n[3] Beides\n")
if len(option) < 1 : option = 3
option = int(option)

# Lese Titelzeile
handle = open(name, 'r')
for line in handle:
    if line.split(";")[0] == "ZirkelID":
        title = line
        break

# Falls Serienbriefausgabe, finde als erstes die Spaltennummer der zugehörigen Spalte.
title = title.strip().split(";")
if option == 2 or option == 3:
    for entry in title:
        if entry in serienbrief_titel:
            serienbrief_titel[entry] = title.index(entry)

# Erzeuge Liste der Zirkel
list_of_ids = []
for line in handle:
    content = line.split(";")
    if content[0] == "ZirkelID":
        continue
    elif content[0] in list_of_ids:
        continue
    elif len(content[0]) > 0:
        list_of_ids.append(content[0])
handle.close()

# Erzeuge csv Dateien fuer jeden Zirkel. Die Schleife laeuft absurd oft, ist aber egal fuer unsere Anwendungen.
for zirkel in list_of_ids:
    handle = open(name, 'r')
    if option == 1 or option  == 2:
        datei = codecs.open(pfad + zirkel + '.csv','w+','utf-8-sig') # Lege Datei an fuer neuen Zirkel
    if option == 3:
        datei_serienbrief = codecs.open(pfad + zirkel + '-brief.csv','w+','utf-8-sig') # Lege Datei an für Serienbrief fuer neuen Zirkel
        datei_gesamt = codecs.open(pfad + zirkel + '.csv','w+','utf-8-sig') # Lege Datei an für   Gesamtliste fuer neuen Zirkel
    if option == 1:
        datei.write(";".join(title).decode('UTF-8') + "\n") # Fuege Titelleiste hinzu
    elif option == 2:
        datei.write(";".join(serienbrief_titel_reihenfolge).decode('UTF-8') + "\n") # Fuege Titelleiste hinzu
    elif option == 3:
        datei_gesamt.write(";".join(title).decode('UTF-8') + "\n") # Fuege Titelleiste hinzu
        datei_serienbrief.write(";".join(serienbrief_titel_reihenfolge).decode('UTF-8') + "\n") # Fuege Titelleiste hinzu
    for line in handle:
        line = line.split(";")
        if line[0] == zirkel:
            if option == 1:
                datei.write(";".join(line).decode('UTF-8'))
            elif option == 2:
                aktuelle_zeile = []
                for i in serienbrief_titel_reihenfolge:
                    aktuelle_zeile.append(line[serienbrief_titel[i]])
                datei.write(";".join(aktuelle_zeile).decode('UTF-8') + "\n")
            elif option == 3:
                datei_gesamt.write(";".join(line).decode('UTF-8'))
                aktuelle_zeile = []
                for i in serienbrief_titel_reihenfolge:
                    aktuelle_zeile.append(line[serienbrief_titel[i]])
                datei_serienbrief.write(";".join(aktuelle_zeile).decode('UTF-8') + "\n")
    
    # Schliesse Dateien fuer aktuellen Zirkel            
    handle.close()
    if option == 1 or option == 2:
        datei.close() 
    if option == 3:
        datei_serienbrief.close()
        datei_gesamt.close()
