from conexion_module.conexion import Conexion
from modelo.comestible import Comestible
from modelo.bebestible import Bebestible
from modelo.mesa import Mesa
from modelo.venta import Venta

class Controlador_datos:
    def __init__(self):
        self.comestibles = []
        self.bebestibles = []
        self.mesas = []
        self.ventas = []
        self.total = 0
    
    def cargar_comestibles(self):
        conn = Conexion()
        
        for comestible in conn.getComestibles():
            comida = Comestible()
            comida.id_comestible = comestible[0] 
            comida.nombre_comestible = comestible[1]
            comida.precio = comestible[2]
            json = {"id_comestible" : comida.id_comestible,
            "nombre_comestible" : comida.nombre_comestible,
            "precio" : comida.precio}
            self.comestibles.append(json)
        return self.comestibles;

    def cargar_bebestibles(self):
        conn = Conexion()

        for bebestible in conn.getBebestibles():
            bebida = Bebestible()
            bebida.id_bebestible = bebestible[0]
            bebida.nombre_bebestible = bebestible[1]
            bebida.precio = bebestible[2]
            json = {"id_bebestible" : bebida.id_bebestible,
            "nombre_bebestible" : bebida.nombre_bebestible,
            "precio" : bebida.precio}
            self.bebestibles.append(json)
        return self.bebestibles

    def cargar_ventas(self):
        conn = Conexion()

        for venta in conn.getVenta():
            ven = Venta()
            ven.id_venta = venta[0]
            ven.id_mesa = venta[1]
            ven.total = venta[2]
            json = {
                "id_venta" : ven.id_venta,
                "id_mesa" : ven.id_mesa,
                "total" : ven.total
            }
            self.ventas.append(json)
        return self.ventas

    def buscar_venta(self, id_venta):
        conn = Conexion()

        for venta in conn.getVenta():
            ven = Venta()
            if venta[0] == id_venta:
                ven.id_venta = venta[0]
                ven.id_mesa = venta[1]
                ven.total = venta[2]
                json = {
                    "id_venta" : ven.id_venta,
                    "id_mesa" : ven.id_mesa,
                    "total" : ven.total
                }
        return json

    def cargar_mesas(self):
        conn = Conexion()

        for mesa in conn.getMesa():
            m = Mesa()
            m.id_mesa = mesa[0]
            m.numero_mesa = mesa[1]
            json = {
                "id_mesa" : m.id_mesa,
                "numero_mesa" : m.numero_mesa
            }
            self.mesas.append(json)
        return self.mesas

    def buscar_comestible(self, id_comestible):
        conn = Conexion()
        
        for comestible in conn.getComestibles():
            c = Comestible()
            if comestible[0] == id_comestible:
                c.id_comestible = comestible[0]
                c.nombre_comestible = comestible[1]
                c.precio = comestible[2]
                json = {
                    "id_comestible" : c.id_comestible,
                    "nombre_comestible" : c.nombre_comestible,
                    "precio" : c.precio 
                }
        return json
    

    def buscar_bebestible(self, id_bebestible):
        conn = Conexion()
        
        for bebestible in conn.getBebestibles():
            b = Bebestible()
            if bebestible[0] == id_bebestible:
                b.id_bebestible = bebestible[0]
                b.nombre_bebestible = bebestible[1]
                b.precio = bebestible[2]
                json = {
                    "id_bebestible" : b.id_bebestible,
                    "nombre_bebestible" : b.nombre_bebestible,
                    "precio" : b.precio 
                }
        return json


    def buscar_mesa(self, id_mesa):
        conn = Conexion()

        for mesa in conn.getMesa():
            m = Mesa()
            if mesa[0] == id_mesa:
                m.id_mesa = mesa[0]
                m.numero_mesa = mesa[1]
                json = {
                    "id_mesa" : m.id_mesa,
                    "numero_mesa" : m.numero_mesa
                }
            
        return json

    def guardar_venta(self, mesa, total):
        conn = Conexion()
        if mesa and total:
            conn.postVenta(mesa, total)
            return True
        else:
            return False