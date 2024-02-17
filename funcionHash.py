import random
import string
import time, datetime

productos = []
personas = []

def convertirAHash(ccDueno, ccComprador, fecha, idproducto):
    hashccDueno = sum([ord(x) for x in ccDueno])
    hashccComprador = sum([ord(x) for x in ccComprador])
    hashFecha = sum([ord(x) for x in "eNeRo"])
    hashIdProducto = sum([ord(x) for x in idproducto])
    print(hashccDueno, hashccDueno, hashFecha, hashIdProducto)

print(ord("a"))
print(ord("b"))
print(sum([ord(x) for x in "ab"]))


print(datetime.datetime.now())



convertirAHash("123", "123", "hi", "qrt")
convertirAHash()




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

print([x.nombre for x in personas])




tiempoAntes = time.time()

for x in range(10):
    producto = {
        "id": x,
        "nombre": "".join([random.choice(string.ascii_lowercase) for x in range(3)]),
        "precio": random.randint(100000, 999999),
        "dueno": (random.choice(personas)).cc
    }
    productos.append(producto)

print(productos)


"""
idABuscar = 799999

tiempoDespues = time.time()

print(f"Crear Productos: {tiempoDespues - tiempoAntes}")

#

tiempoAntes = time.time()

for producto in productos:
    encontrado = False
    if producto.get("id") == idABuscar:
        print(producto)#info del producto
        encontrado = True
        break

if not encontrado:
    print("no encontrado")

tiempoDespues = time.time()

print(f"Busqueda Secuencial: {tiempoDespues - tiempoAntes}")

#

#

tiempoAntes = time.time()

while(True):
    pivote = int((len(productos)-1)/2)
    #print(f"pivote {pivote}")
    idDatoEnPivote = productos[pivote].get("id")
    #print(idDatoEnPivote)
    #print(f"iDpivote {idPivote}")
    #time.sleep(0.5)
    if idDatoEnPivote == idABuscar:
        print(productos[pivote])
        break
    #if(productos[pivote+1].get("id")) > idABuscar:
    if idDatoEnPivote > idABuscar:
        productos = productos[:pivote]
    else:
        productos = productos[pivote+1:]
    #print(productos)
    if not productos:
        print("no encontrado")
        break

tiempoDespues = time.time()

print(f"Busqueda Binaria: {tiempoDespues - tiempoAntes}")

#

"""
