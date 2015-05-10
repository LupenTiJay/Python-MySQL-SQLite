#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","server","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to DELETE required records
sql = "DELETE FROM METRIC WHERE id < '%d'" % (1000)
sqlVONE = "DELETE FROM VONE WHERE OCCURANCES < '%d'" % (1000)
sqlDC 	= "DELETE FROM DC WHERE OCCURANCES < '%d'" % (1000)
sqlECTWO = "DELETE FROM ECTWO WHERE OCCURANCES < '%d'" % (1000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   cursor.execute(sqlVONE)
   cursor.execute(sqlDC)
   cursor.execute(sqlECTWO)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
