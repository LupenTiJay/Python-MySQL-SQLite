import ftplib, os, os.path
#import urllib
session = ftplib.FTP('172.16.50.12', 'metric', 'C12r47Wv')

print ("connected to server...")

#file = open('test.gif', 'rb')
#session.storbinary('STOR test.gif', file)
#file.close
session.dir()

filenames = session.nlst()
#print (filenames)

#for filename in filenames:
	##local_filename = os.path.join('/mnt/v1desk/metric', filename)
	#file = open(filename, 'wb')
	#session.retrbinary('RETR '+filename, file.write)
	#file.close

#counter =0;	
#for filename in filenames:
#	ff = filename[:6]
#	if ff != "METRIC":
#		print (ff)
		#print("HELOO")
#		filenames.remove(filename)
	#counter += 1

#print (filenames)
	
download = filenames[0]
d1 = download[25:]
year = int(d1[:4])
month = int(d1[5:7])
day = int(d1[8:10])
for f1 in filenames:
	ff = f1[:6]
	if ff == "METRIC":
		#print(ff)
		g = f1
		g1 = f1[25:]
		current_year = int(g1[:4])
		current_month = int(g1[5:7])
		current_day = int(g1[8:10])
		
		#print (current_day)
		#print (current_month)
		#print (month)
		#print (current_year)
		#print(year)
		
		if current_year > year:
			#print ("99999")
			download = g
		elif current_month > month and current_year == year:
			#print("888888")
			download = g
		elif current_day > day and current_month == month:
			#print("77777")
			download = g
		#print("================================================")

#print (download)			
			
file2 = open(download, 'wb')
session.retrbinary('RETR '+download, file2.write)
file2.close
	
#urllib.request.urlretrieve('ftp://172.16.50.12/mnt/v1desk/metric', 'test.gif')
session.quit()
