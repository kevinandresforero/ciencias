import random
import string
import time

productos = []

tiempoAntes = time.time()

for x in range(800000):
    producto = {
        "id": x,
        "nombre": "".join([random.choice(string.ascii_lowercase) for x in range(3)]),
        "precio": random.randint(100000, 999999)
    }
    productos.append(producto)

#print(productos)

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

