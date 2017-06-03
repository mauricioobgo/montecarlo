
import sqlite3
class dbManager():
    """docstring for dbManager"""
    def __init__(self, arg):
        self.conn=""
        self.dbAdd=""


    def connectionInitiator(self):
        self.conn=sqlite3.connect('price_history.db')
        self.dbAdd=self.conn.cursor()


    def createTable(self):
        self.connectionInitiator()
        self.dbAdd.execute("CREATE TABLE IF NOT EXISTS history(nemo TEXT, isin TEXT, tipo TEXT, fecha_archivo TEXT,"+
        "fecha_emision TEXT, fecha_vencimiento TEXT, fondo TEXT, moneda TEXT, tipo_tasa TEXT, digits2 REAL, precio_limpio REAL, precio_sucio REAL)")
        self.conn.commit()


    def insertInfo(self,nemo,isin,tipo,fecha_archivo,fecha_emision,fecha_vencimiento,fondo,moneda,tipo_tasa,digits2,precio_limpio,precio_sucio):
         self.dbAdd.execute("INSERT INTO history (nemo,isin,tipo,fecha_archivo,fecha_emision,fecha_vencimiento,fondo,moneda,tipo_tasa,digits2,precio_limpio,precio_sucio) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (nemo,isin,tipo,fecha_archivo,fecha_emision,fecha_vencimiento,fondo,moneda,tipo_tasa,digits2,precio_limpio,precio_sucio))
         self.conn.commit()
         
    def closeConnection(self):
        self.dbAdd.close()
        self.conn.close()

    def queryDate(self,date):
        self.dbAdd.execute("SELECT COUNT(*) FROM history where fecha_archivo ='"+ date +"'")
        data=self.dbAdd.fetchall()
        print(data)
        if(data[0][0]>0):
            return True
        else:
            return False
        
        
        