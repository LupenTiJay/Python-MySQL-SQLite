#/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import time
import MySQLdb
con = lite.connect('metric.db')
array = []
word = []
with con:

	cur = con.cursor()
	cur.execute("SELECT * FROM metric")

	rows = cur.fetchall()

	for row in rows:
		
		array.append(str(row))
		#print row
		
	# remove bracket
	for x in range (0, len(array)):
		print "Echo"
		for ch in ['(',')']:
				array[x] = array[x].replace(ch,"")
				#print array[x]
	#Split at ,
	for x in range(0, len(array)):
		print array[x]
		word = array[x].split(',')
		word[4] = word[4].replace("\n","")
		word[3] = word[3].replace("\n","")

		if len(word)>5:
			for c in range(5,len(word)):
				word[5] = word[5] + word[c]
		for v in range(0,5):
			print "-----"
			print word[v]

		word[0] = word[0]
		word[1] = word[1][3:-1]
		word[2] = word[2][3:-1]
		word[3] = word[3][3:-1]
		word[4]	= word[4][3:-1]

		# Open database connection
		db = MySQLdb.connect("localhost","root","server","TESTDB" )
		# prepare a cursor object using cursor() method
		print "*****"
		print word[0]
		print word[1]
		print word[2]
		print word[3]
		print word[4]
		print "*****"
		cursor = db.cursor()

		# Prepare SQL query to INSERT a record into the database.
		test = "(%s, %s, %s, %s, %s)" % ("1", word[1], word[2], word[3], word[4])
		sql = """INSERT INTO METRIC(ID,
		         LOCATION, METHOD, SERVICE, TIME)
		         VALUES ({4}, '{0}', '{1}', '{2}', '{3}')""".format(word[1], word[2], word[3], word[4], word[0])
		try:
		   # Execute the SQL command
		   cursor.execute(sql)
		   # Commit your changes in the database
		   db.commit()
		except:
		   # Rollback in case there is any error
		   db.rollback()
		   print "NOT WORKING"

		# disconnect from server
	db.close()	

			


	