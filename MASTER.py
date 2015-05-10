import os

file = open('Parameter', 'r')
Parameter = []
for line in file:
    print line,
    Parameter.append(line.split(':'))

for i in range(0 , len(Parameter)):
	print(Parameter[i][1])
createTableArgv = "{0} {1} {2} {3}".format(Parameter[3][1], Parameter[4][1], Parameter[5][1], Parameter[6][1])
createTableArgv = createTableArgv.replace("\n", "")

SQLITETOMYSQLARGV = "{0} {1}".format(createTableArgv, Parameter[2][1] )

os.system("python CREATETABLE.py {0}".format(createTableArgv))
os.system("python SQLITETOMYSQLRAW.py {0}".format(SQLITETOMYSQLARGV))
os.system("python SQLITETOMYSQLSORTED.py {0}".format(SQLITETOMYSQLARGV))
os.system("python TESTARGV.py test")

