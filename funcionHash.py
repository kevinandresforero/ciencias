import random
import string
import time
import datetime

productos = []
personas = []
transacciones = [None] * 20


def crecerArregloTransacciones(idHash, arregloTransacciones):
    arregloConTamanioCorregido = arregloTransacciones
    if idHash > (len(arregloTransacciones) - 1):
        loQueLeFalta = idHash - (len(arregloTransacciones) - 1)
        #print(loQueLeFalta)
        arregloTemp = [None] * loQueLeFalta
        #print(arregloTemp)
        arregloConTamanioCorregido += arregloTemp
        #print(len(arregloConTamanioCorregido))
    return arregloConTamanioCorregido



def convertirAHash(ccDueno, ccComprador, idproducto):
    primo1 = 31
    primo2 = 37
    primo3 = 41
    primo4 = 43

    # Convertimos cada parte del input en un hash numérico simple sumando los valores ASCII de cada carácter.
    hashccDueno = sum([ord(x) for x in str(ccDueno)]) * primo1
    hashccComprador = sum([ord(x) for x in str(ccComprador)]) * primo2
    #hashFecha = sum([ord(x) for x in fecha]) * primo3
    hashIdProducto = sum([ord(x) for x in str(idproducto)]) * primo4

    # Combinamos los hashes con una operación simple. Podrías elegir otras operaciones para combinar estos valores.
    #hashFinal = hashccDueno + hashccComprador + hashFecha + hashIdProducto
    hashFinal = hashccDueno + hashccComprador + hashIdProducto

    return hashFinal


# Usando datetime.datetime.now() para obtener fecha y hora actual
fecha_hora_actual = str(datetime.datetime.now())


class persona:
    def __init__(self, cc, nombre):
        self.cc = cc
        self.nombre = nombre


personas.append(persona(12310, "Julanito1"))
personas.append(persona(12320, "Julanito2"))
personas.append(persona(12330, "Julanito3"))
personas.append(persona(12340, "Julanito4"))
personas.append(persona(12350, "Julanito5"))
personas.append(persona(12360, "Julanito6"))
personas.append(persona(12370, "Julanito7"))
personas.append(persona(12380, "Julanito8"))
personas.append(persona(12390, "Julanito9"))
personas.append(persona(12310, "Julanito10"))

for x in range(10):
    producto = {
        "id": x,
        "nombre": "".join([random.choice(string.ascii_lowercase) for x in range(3)]),
        "precio": random.randint(100000, 999999),
        "dueno": (random.choice(personas)).cc
    }
    productos.append(producto)


class transaccion:
    def __init__(self, ccDuenoE, ccComprador, idProductoE, anio, mes, dia):
        #self.fecha = fecha_hora_actual = str(datetime.datetime.now())
        self.fecha = "".join([str(anio),str(mes),str(dia)])
        self.id = 1
        """
        self.id = convertirAHash(
            str(ccDuenoE), str(ccComprador), str(idProductoE))
        """
        self.ccDueño = ccDuenoE
        self.ccComprador = ccComprador
        self.idProducto = idProductoE
        self.Siguiente = None

class listaEnlazadaTransacciones:
    def __init__(self):
        self.nodoCabeza = None
        self.nodoCola = None

    def agregarTransaccion(self, objetoTransaccion):
        if self.nodoCola == None:
            self.nodoCola = objetoTransaccion
        else:
            self.nodoCola.Siguiente = objetoTransaccion
            self.nodoCola = objetoTransaccion

        if self.nodoCabeza == None:
            self.nodoCabeza = objetoTransaccion
            self.nodoCabeza.Siguiente = self.nodoCola

linkedListTransacciones = listaEnlazadaTransacciones()


for repeticiones in range(5):
    if productos:
        producto_aleatorio = random.choice(productos)
        # Obtiene el cc del dueño del producto seleccionado
        cc_dueño_producto_aleatorio = producto_aleatorio['dueno']
        # Selecciona un comprador aleatorio diferente al dueño actual
        compradores_potenciales = [
            persona for persona in personas if persona.cc != cc_dueño_producto_aleatorio]
        if not compradores_potenciales:  # Verifica si hay compradores potenciales
            print("No hay compradores potenciales disponibles.")
            exit()
        comprador_aleatorio = random.choice(compradores_potenciales)
        # Crea la transacción con el dueño actual, un comprador aleatorio, y el ID del producto aleatorio
        nueva_transaccion = transaccion(
            cc_dueño_producto_aleatorio, comprador_aleatorio.cc, producto_aleatorio['id'], 2024, 1, 1)
        #idHashTemp = convertirAHash(nueva_transaccion.ccDueño, nueva_transaccion.ccComprador, nueva_transaccion.idProducto)
        idHashTemp = 15000
        #print(idHashTemp)
        print(len(transacciones))
        transacciones = crecerArregloTransacciones(idHashTemp, transacciones)
        print(len(transacciones))
        #transacciones[idHashTemp] = nueva_transaccion
        if transacciones[idHashTemp] == None:
            transacciones[idHashTemp] = listaEnlazadaTransacciones()
            transacciones[idHashTemp].agregarTransaccion(nueva_transaccion)
        else:
            transacciones[idHashTemp].agregarTransaccion(nueva_transaccion)
        
        print(transacciones[idHashTemp-5:idHashTemp +5])
        #linkedListTransacciones.agregarTransaccion(nueva_transaccion)
        #transacciones.append(nueva_transaccion)  # Guarda la nueva transacción // Debeira convertir a hash

        # Actualiza el dueño del producto en la lista de productos
        """
        for producto in productos:
            if producto['id'] == producto_aleatorio['id']:
                # Actualiza el dueño del producto al comprador
                producto['dueno'] = comprador_aleatorio.cc
                break  # Sale del bucle una vez que el producto ha sido actualizado
        """

    else:
        print("No hay productos disponibles para crear una transacción.")

nodoTemp = transacciones[-1].nodoCabeza

while True:
    print(nodoTemp)
    nodoTemp = nodoTemp.Siguiente
    if nodoTemp == linkedListTransacciones.nodoCola:
        break

"""
def imprimir_transacciones(transacciones):
    if not transacciones:
        print("No se han realizado transacciones.")
        return

    for transaccion in transacciones:
        print(f"Transacción ID: {transaccion.id}")
        print(f"Fecha: {transaccion.fecha}")
        # Asegúrate de que el nombre del atributo sea correcto
        print(f"CC Dueño: {transaccion.ccDueño}")
        print(f"CC Comprador: {transaccion.ccComprador}")
        print(f"ID Producto: {transaccion.idProducto}")
        print("-----")


# Llama a la función para imprimir las transacciones
imprimir_transacciones(transacciones)

"""