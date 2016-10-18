import codecs

# Oeffne Tabelle, die per Bericht aus Base exportiert wird. Sie darf als Zwischenzeilen nur solche mit Beginn "ZirkelID" haben.
name = raw_input("Enter file:")
if len(name) < 1 : name = "liste.csv"
handle = open(name, 'r')

# Erzeuge Liste der Zirkel
list_of_ids = []
for line in handle:
    line = line.strip()
    content = line.split(";")
    if content[0] == "ZirkelID":
        continue
    elif content[0] in list_of_ids:
        continue
    elif len(content[0]) > 0:
        list_of_ids.append(content[0])
handle.close()

# Erzeuge csv Dateien fuer jeden Zirkel. Die Schleife laeuft absurd oft, ist aber egal fuer unsere Anwendungen. handle muss neu geladen werden, weil oben eventuelle Leerzeichen von strip() entfernt werde.
for zirkel in list_of_ids:
    file = codecs.open(zirkel + '.csv','w+','utf-8-sig') # Lege Datei an fuer neuen Zirkel
    handle = open(name, 'r')
    for line in handle:
        line = line.strip()
        #print "zirkel = " + zirkel + "\n"
        #print "anfang zeile = " + line.split(";")[0] + "\n"        
        if line.split(";")[0] == zirkel:
            #print "".join(line)
            file.write("".join(line).decode('UTF-8') + "\n")
    handle.close()
    file.close() # Schliesse Datei fuer aktuellen Zirkel
