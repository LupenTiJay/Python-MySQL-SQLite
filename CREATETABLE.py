#!/usr/bin/python
import MySQLdb
from sys import argv
script, ip, user, password, database, = argv
"""
ip = 'localhost'
user = 'root'
password = 'server'
database = 'TESTDB'
sqliteFile = 'metric.db'
"""


#print script
print ip
print user
print password
print database

#db = MySQLdb.connect("localhost{0}","root{1}","server{2}","TESTDB{3}".format(ip, user, password, database) )
db = MySQLdb.connect("%s" % ip,"%s" % user,"%s" % password,"%s" % database)

cursor = db.cursor();


##############
cursor.execute("DROP TABLE IF EXISTS METRIC")

sql = """CREATE  TABLE METRIC (ID int(50),
		LOCATION CHAR(100), 
		METHOD CHAR(100),
		SERVICE CHAR(50), 
		TIME CHAR(30))"""

cursor.execute(sql)

###############
cursor.execute("DROP TABLE IF EXISTS SORTOCCURENCES")
 
sql = """CREATE TABLE SORTOCCURENCES (DATE CHAR(100), 
		Village1 int, 
		DavisCenter int,
		EastCampus int)"""

cursor.execute(sql)


#############
#cursor.execute("DROP TABLE IF EXISTS DC")

#sql = """ CREATE TABLE DC (LOCATION CHAR (100), OCCURENCES int(50))"""

#cursor.execute(sql)

#############
#cursor.execute("DROP TABLE IF EXISTS ECTWO")

#sql = """ CREATE TABLE ECTWO (LOCATION CHAR (100), OCCURENCES int(50))"""

#cursor.execute(sql)



db.close
