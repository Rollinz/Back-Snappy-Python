import pymysql
from conexion_module.consultas import consulta_comestible, consulta_bebestible, consulta_mesa, consulta_venta, crearVenta, host, user, password, db

class Conexion:
# Cursor para rescatar datos
    
    def __init__(self):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        
    def getComestibles(self):
        # Consulta SQL
        db = pymysql.connect(self.host, self.user, self.password, self.db)
        cursor = db.cursor();
        cursor.execute(consulta_comestible)    
        results = cursor.fetchall()
        db.close()
        return results

    def getBebestibles(self):
        db = pymysql.connect(self.host, self.user, self.password, self.db)
        cursor = db.cursor();
        cursor.execute(consulta_bebestible)    
        results = cursor.fetchall()
        db.close()
        return results
    
    def getMesa(self):
        db = pymysql.connect(self.host, self.user, self.password, self.db)
        cursor = db.cursor();
        cursor.execute(consulta_mesa)    
        results = cursor.fetchall()
        db.close()
        return results

    def getVenta(self):
        db = pymysql.connect(self.host, self.user, self.password, self.db)
        cursor = db.cursor();
        cursor.execute(consulta_venta)    
        results = cursor.fetchall()
        db.close()
        return results

    def postVenta(self, mesa, total):
        estado = False
        db = pymysql.connect(self.host, self.user, self.password, self.db)
        try:
            cursor = db.cursor();
            cursor.execute(crearVenta(mesa, total))
            db.commit()
            db.close()
            estado = True
        except:
            db.rollback()
        return estado