from controlador.controlador_datos import Controlador_datos
from modelo.mesa import Mesa
from modelo.venta import Venta
from flask import Flask, jsonify, Request, request

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message":"pong"})

@app.route("/comestibles", methods=['GET'])
def getComestibles():
    control = Controlador_datos()
    return jsonify(control.cargar_comestibles())

@app.route("/bebestibles", methods=['GET'])
def getBebestibles():
    control = Controlador_datos()
    return jsonify(control.cargar_bebestibles())

@app.route("/mesas", methods=['GET'])
def getMesas():
    control = Controlador_datos()
    return jsonify(control.cargar_mesas())

@app.route("/mesas/<int:id_mesa>", methods=['GET'])
def getMesa(id_mesa):
    control = Controlador_datos()
        
    mesa = control.buscar_mesa(id_mesa)
    #mesaEncontrada = [mesa for mesa in control.cargar_mesas if mesa['id_mesa']==id_mesa]

    return jsonify({"mesa": mesa})

@app.route("/comestibles/<int:id_comestible>", methods=['GET'])
def getComestible(id_comestible):
    control = Controlador_datos()

    comestible = control.buscar_comestible(id_comestible)
    return jsonify({"comestible": comestible})

@app.route("/bebestibles/<int:id_bebestible>", methods=['GET'])
def getBebestible(id_bebestible):
    control = Controlador_datos()

    bebestible = control.buscar_bebestible(id_bebestible)
    return jsonify({"comestible": bebestible})

@app.route("/ventas", methods=['GET'])
def getVentas():
    control = Controlador_datos()
    return jsonify(control.cargar_ventas())

@app.route("/ventas/<int:id_venta>", methods=['GET'])
def getVenta(id_venta):
    control = Controlador_datos()
    venta = control.buscar_venta(id_venta)
    return jsonify({"venta" : venta})

@app.route("/ventas", methods=['POST'])
def addVenta():
    control = Controlador_datos()

    venta = Venta()
    venta.id_mesa = request.json['id_mesa']
    venta.total = request.json['total']

    print(venta.total)
    if control.guardar_venta(venta.id_mesa, venta.total):
        return "Venta exitosa"
        getVentas()
    else:
        return "Hubo un error"        
if __name__ == '__main__':
    app.run(debug=True, port=4000)

# control = Controlador_datos()

# for x in control.cargar_comestibles():
#     print(x.nombre_comestible)