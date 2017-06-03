import mysql.connector
from mysql.connector import errorcode

class sqlManager():
    

    def __init__(self,nueva):
        self.connectVarible=nueva
    
    
    #Método de conexión a base de datos
    def connection(self):
        print("echo")
        result=""
        try:
            print("llegué")
            cnn=mysql.connector.connect(user='root',password='root',host='localhost',database='playground')
            result= cnn
        except mysql.connector.Error as e:
            if e.errno==errorcode.ER_ACCESS_DENIED_ERROR:
                result="something is wrong with user name or password"
            elif e.errno==errorcode.ER_BAD_DB_ERROR:
                result="the database does not exists"
            else:
                result=e
        return result                

    def insertVaalues(self):
        print("echo")
        valor=self.connection()
        print("it Works")
        valor.close()
        print(valor)