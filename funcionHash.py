import random
import string
import time
import datetime

productos = []
personas = []
transacciones = []


def convertirAHash(ccDueno, ccComprador, idproducto, fecha):
    primo1 = 31
    primo2 = 37
    primo3 = 41
    primo4 = 43

    # Convertimos cada parte del input en un hash numérico simple sumando los valores ASCII de cada carácter.
    hashccDueno = sum([ord(x) for x in ccDueno]) * primo1
    hashccComprador = sum([ord(x) for x in ccComprador]) * primo2
    hashFecha = sum([ord(x) for x in fecha]) * primo3
    hashIdProducto = sum([ord(x) for x in idproducto]) * primo4

    # Combinamos los hashes con una operación simple. Podrías elegir otras operaciones para combinar estos valores.
    hashFinal = hashccDueno + hashccComprador + hashFecha + hashIdProducto

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
    def __init__(self, ccDuenoE, ccComprador, idProductoE):
        self.fecha = fecha_hora_actual = str(datetime.datetime.now())
        self.id = convertirAHash(
            str(ccDuenoE), str(ccComprador), str(idProductoE), self.fecha)
        self.ccDueño = ccDuenoE
        self.ccComprador = ccComprador
        self.idProducto = idProductoE


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
        cc_dueño_producto_aleatorio, comprador_aleatorio.cc, producto_aleatorio['id'])
    transacciones.append(nueva_transaccion)  # Guarda la nueva transacción

    # Actualiza el dueño del producto en la lista de productos
    for producto in productos:
        if producto['id'] == producto_aleatorio['id']:
            # Actualiza el dueño del producto al comprador
            producto['dueno'] = comprador_aleatorio.cc
            break  # Sale del bucle una vez que el producto ha sido actualizado

else:
    print("No hay productos disponibles para crear una transacción.")


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
