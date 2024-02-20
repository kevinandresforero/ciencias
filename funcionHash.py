import random
import string
import time
import datetime

productos = []
personas = []


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


def encontrar_duenos_de_productos(productos, personas):
    duenos = []  # Lista para guardar los dueños encontrados
    for producto in productos:
        cc_dueno = producto["dueno"]
        for persona in personas:
            if persona.cc == cc_dueno:
                duenos.append(persona)
                break  # Rompe el loop interno una vez que encuentres al dueño
    return duenos


duenos = encontrar_duenos_de_productos(productos, personas)
for dueno in duenos:
    print(f"Dueño: {dueno.nombre}, CC: {dueno.cc}")


class transaccion:
    def __init__(self, ccDueño, ccComprador, idProducto):
        self.fecha = fecha_hora_actual = str(datetime.datetime.now())
        self.id = convertirAHash(ccDueno, ccComprador, idproducto, self.fecha)
        self.ccDueño = ccDueño
        self.ccComprador = ccComprador
        self.idProducto = idProducto
