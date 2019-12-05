consulta_comestible = "select * from comestible"
consulta_bebestible = "select * from bebestible"
consulta_mesa = "select * from mesa"
consulta_venta = "select * from venta"

# conexion de base de datos
host = "localhost"
user = "root"
password = ""
db = "snappy"

def crearVenta(mesa, total):
    insertar_venta = "insert into venta (id_mesa, total) values ('{0}','{1}')".format(mesa, total)
    return insertar_venta