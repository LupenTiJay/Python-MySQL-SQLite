#/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite # library with reading/writing/processing sqlite module
import sys
import MySQLdb
#import time
con = lite.connect('metric.db') # connects to  sqlite file named metric located in the same directory as this script
holdData = [] 
word = []
display = []
with con:
	#retrieves all the data
	cur = con.cursor()
	cur.execute("SELECT * FROM metric")
	sqliteData = cur.fetchall()

	#print sqliteData
	for row in sqliteData:
		
		holdData.append(str(row))
		#print row
		
	# remove bracket
	for x in range (0, len(holdData)):
		print "Echo"
		for ch in ['(',')']:
				holdData[x] = holdData[x].replace(ch,"")
				#print holdData[x]
	#Split at ,
	for x in range(0, len(holdData)):
		print holdData[x]
		word = holdData[x].split(',')
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

		display.append(word)



#Seperating table into V1 and DC and EC@
vOne = []
dC = []
eCTWO = []
for z in range( 0, len(display)):
	if(display[z][2]=='Village 1'):
		display[z][1] = display[z][1][:10]
		vOne.append(display[z])

	elif(display[z][2]=='Davis Center'):
		display[z][1] = display[z][1][:10]
		dC.append(display[z])

	else:
		display[z][1] = display[z][1][:10]
		eCTWO.append(display[z])


VOneCounter = []
dCcounter = []
eCTWOcounter = []

counter = 0
for z in range(0, len(vOne)):
	#print vOne[z]
	#print "###"
	if(z + 1 < len(vOne)):
		if(vOne[z][1]== vOne[z+1][1] ):
			counter = counter + 1

		else:
			temp = [[vOne[z][1]], [counter + 1]]
			VOneCounter.append(temp)
			counter = 0


for z in range(0, len(dC)):
	print dC[z]
	print "###"
	print z
	if(z + 1 < len(dC)):
		if(dC[z][1]== dC[z+1][1] ):
			counter = counter + 1

		else:
			temp = [[dC[z][1]], [counter + 1]]
			dCcounter.append(temp)
			counter = 0

	else:
		temp = [[dC[z][1]], [counter ]]
		dCcounter.append(temp)

print len(dCcounter)
for z in range(0, len(eCTWO)):
	#print eCTWO[z]
	#print "###"
	if(z + 1 < len(eCTWO)):
		if(eCTWO[z][1]== eCTWO[z+1][1] ):
			counter = counter + 1

		else:
			temp = [[eCTWO[z][1]], [counter + 1]]
			eCTWOcounter.append(temp)
			counter = 0

# for test print purposes
"""
for z in range(0, len(VOneCounter)):
	print VOneCounter[z]
	print "!!!!!"

for z in range(0, len(dCcounter)):
	print dCcounter[z]
	print "@@@@@"

for z in range(0, len(eCTWOcounter)):
	print eCTWOcounter[z]
	print "#####"
"""

db = MySQLdb.connect("localhost","root","server","TESTDB" )

cursor = db.cursor()

for z in range(0, len(VOneCounter)):
	sql = """INSERT INTO VONE(
	         LOCATION, OCCURANCES)
	         VALUES ('{0}', '{1}')""".format(VOneCounter[z][0][0], VOneCounter[z][1][0])
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()
	   print "NOT WORKING"


############

for z in range(0, len(dCcounter)):
	sql = """INSERT INTO DC(
	         LOCATION, OCCURANCES)
	         VALUES ('{0}', '{1}')""".format(dCcounter[z][0][0], dCcounter[z][1][0])
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()
	   print "NOT WORKING"	   

############

for z in range(0, len(eCTWOcounter)):
	sql = """INSERT INTO ECTWO(
	         LOCATION, OCCURANCES)
	         VALUES ('{0}', '{1}')""".format(eCTWOcounter[z][0][0], eCTWOcounter[z][1][0])
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





















