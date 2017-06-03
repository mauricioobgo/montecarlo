

import mysql.connector
from mysql.connector import errorcode

class sqlManager():

   


	__init__(self):
   		self.connectVarible=connection()  
   		connectVarible.close()


def connection:
	try:
	 cnn=mysql.connector.connect(
         user='root',
         password='root',
         host='localhost',
         database='playground'
	 	)
	 print('it works')
    return cnn
	except mysql.connector.Error as e:
		if e.errno==errorcode.Er_ACCESS_DENIED_ERROR:
			print("something is wron with user name or password")
		elif e.errno=errorcode.ER_BAD_DB_ERROR:
			print("the database does not exists")

