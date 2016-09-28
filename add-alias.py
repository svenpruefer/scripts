#!/usr/bin/python

import MySQLdb

# Ask for root password in mysql
passwd = raw_input("Enter password for user root in mysql: ")

# Open database connection
db = MySQLdb.connect("localhost","root", passwd,"servermail" )

# Input file to read from
filename = raw_input("Enter file to read for entries: ")
fh = open(filename)

# Enter name of mailing list
alias = raw_input("Enter name of alias: ")

# prepare a cursor object using cursor() method
cursor = db.cursor()

for line in fh:
    line = line.strip()
    
    # Read last id number
    # cursor.execute("SELECT * FROM virtual_aliases") 
    # id = cursor.rowcount + 1
    
    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO virtual_aliases (domain_id, source, destination) \
           VALUES ('%d', '%s', '%s')" % \
           (1, alias, line)
    
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

# disconnect from server
db.close()
