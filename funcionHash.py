import random
import string
import time
import datetime

productos = []
personas = []


def convertirAHash(ccDueno, ccComprador, fecha, idproducto):
    hashccDueno = sum([ord(x) for x in ccDueno])
    hashccComprador = sum([ord(x) for x in ccComprador])
    hashFecha = sum([ord(x) for x in fecha])
    hashIdProducto = sum([ord(x) for x in idproducto])
    return hashccDueno+hashccComprador+hashFecha+hashIdProducto


# Usando datetime.datetime.now() para obtener fecha y hora actual
fecha_hora_actual = str(datetime.datetime.now())

print(convertirAHash("123", "123", fecha_hora_actual, "qrt"))


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


tiempoAntes = time.time()

for x in range(10):
    producto = {
        "id": x,
        "nombre": "".join([random.choice(string.ascii_lowercase) for x in range(3)]),
        "precio": random.randint(100000, 999999),
        "dueno": (random.choice(personas)).cc
    }
    productos.append(producto)


class transaccion:
    def __init__(self, ccDueño, ccComprador):
        self.id = ccDueño + ccComprador + str(datetime.datetime)
        self.detalle = ccDueño + ccComprador + str(datetime.datetime)
