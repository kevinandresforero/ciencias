import random
import string

class persona:
    def __init__(self, cc, nombre):
        self.cc = cc
        self.nombre = nombre

class transaccion:
    def __init__(self, ccDuenoE, ccComprador, idProductoE, anio, mes, dia):
        self.fecha = "".join([str(anio), str(mes), str(dia)])
        self.id = random.randint(1000, 9999)
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


def crecerArregloTransacciones(idHash, arregloTransacciones):
    arregloConTamanioCorregido = arregloTransacciones
    if idHash > (len(arregloTransacciones) - 1):
        loQueLeFalta = idHash - (len(arregloTransacciones) - 1)
        arregloTemp = [None] * loQueLeFalta
        arregloConTamanioCorregido += arregloTemp
    return arregloConTamanioCorregido


def convertirAHash(ccDueno, ccComprador, idproducto):
    primo1 = 31
    primo2 = 37
    primo3 = 41
    primo4 = 43

    # Convertimos cada parte del input en un hash numérico simple sumando los valores ASCII de cada carácter.
    hashccDueno = sum([ord(x) for x in str(ccDueno)]) * primo1
    hashccComprador = sum([ord(x) for x in str(ccComprador)]) * primo2
    # hashFecha = sum([ord(x) for x in fecha]) * primo3
    hashIdProducto = sum([ord(x) for x in str(idproducto)]) * primo4

    # Combinamos los hashes con una operación simple. Podrías elegir otras operaciones para combinar estos valores.
    # hashFinal = hashccDueno + hashccComprador + hashFecha + hashIdProducto
    hashFinal = hashccDueno + hashccComprador + hashIdProducto

    return hashFinal

def crearTransaccion(arregloPersonas, arregloTransacciones, arregloProductos, anio, mes, dia):
    if arregloProductos:
        producto_aleatorio = random.choice(arregloProductos)
        # Obtiene el cc del dueño del producto seleccionado
        cc_dueño_producto_aleatorio = producto_aleatorio['dueno']
        # Selecciona un comprador aleatorio diferente al dueño actual
        compradores_potenciales = [
            persona for persona in arregloPersonas if persona.cc != cc_dueño_producto_aleatorio]
        if not compradores_potenciales:  # Verifica si hay compradores potenciales
            print("No hay compradores potenciales disponibles.")
            exit()
        comprador_aleatorio = random.choice(compradores_potenciales)
        # Crea la transacción con el dueño actual, un comprador aleatorio, y el ID del producto aleatorio
        nueva_transaccion = transaccion(
            cc_dueño_producto_aleatorio, comprador_aleatorio.cc, producto_aleatorio['id'], anio, mes, dia)
        idHashTemp = convertirAHash(nueva_transaccion.ccDueño, nueva_transaccion.ccComprador, nueva_transaccion.idProducto)
        #idHashTemp = 15000
        testigos.append(idHashTemp)
        #print(cc_dueño_producto_aleatorio, comprador_aleatorio.cc)
        # print(idHashTemp)
        #print(len(arregloTransacciones))
        arregloTransacciones = crecerArregloTransacciones(idHashTemp, arregloTransacciones)
        #print(len(arregloTransacciones))
        # transacciones[idHashTemp] = nueva_transaccion
        if arregloTransacciones[idHashTemp] == None:
            arregloTransacciones[idHashTemp] = listaEnlazadaTransacciones()
            arregloTransacciones[idHashTemp].agregarTransaccion(nueva_transaccion)
        else:
            arregloTransacciones[idHashTemp].agregarTransaccion(nueva_transaccion)

        # linkedListTransacciones.agregarTransaccion(nueva_transaccion)
        # transacciones.append(nueva_transaccion)  # Guarda la nueva transacción // Debeira convertir a hash
        # Actualiza el dueño del producto en la lista de productos
        for producto in productos:
            if producto['id'] == producto_aleatorio['id']:
                # Actualiza el dueño del producto al comprador
                producto['dueno'] = comprador_aleatorio.cc
                break  # Sale del bucle una vez que el producto ha sido actualizado

    else:
        print("No hay productos disponibles para crear una transacción.")

def imprimirTransaccion(transaccion):
    print(f"Transacción ID: {transaccion.id}")
    print(f"Fecha: {transaccion.fecha}")
    print(f"CC Dueño: {transaccion.ccDueño}")
    print(f"CC Comprador: {transaccion.ccComprador}")
    print(f"ID Producto: {transaccion.idProducto}")


def imprimir_transacciones(transacciones):

    for indice in range(len(transacciones)):
        if transacciones[indice] is not None:
            nodoTemp = transacciones[indice].nodoCabeza
            while(True):
                imprimirTransaccion(nodoTemp)
                print(f"hash ID: {indice}")
                print(transacciones[indice - 5:indice + 5], f"Posicion en arreglo: {indice}")
                print("-----")
                if nodoTemp == transacciones[indice].nodoCola:
                    break
                else:
                    nodoTemp = nodoTemp.Siguiente


def modificarTransaccionRandom(arregloTransacciones, arregloTestigos):
    arregloTransaccionesValidas = []
    arregloListasValidas = [x for x in arregloTransacciones if x is not None]

    for lista in arregloListasValidas:
        nodoTemp = lista.nodoCabeza
        while(True):
            arregloTransaccionesValidas.append(nodoTemp)
            if nodoTemp == lista.nodoCola:
                break
            else:
                nodoTemp = nodoTemp.Siguiente
    #print(arregloListasValidas)
    #print(arregloTransaccionesValidas)
    transaccionRandom = random.choice(arregloTransaccionesValidas)
    imprimirTransaccion(transaccionRandom)
    hashCalculado = convertirAHash(transaccionRandom.ccDueño, transaccionRandom.ccComprador, transaccionRandom.idProducto)
    #hashCalculado = 15000
    print(f"El hash es {hashCalculado}, SOLO SE MUESTRA PARA FINES DEMOSTRATIVOS PARA COMPROBAR UN HASH VALIDO")
    hashUsuario = None
    while (True):
        try:
            hashUsuario = int(input("Para guardar su modificacion, Digite el hash: "))
            valido = True
        except ValueError:
            print("No valido")
            valido = False
        if valido:
            break
    if hashUsuario not in arregloTestigos:
        print(f"No es valido modificar, hash invalido")
    elif hashUsuario in arregloTestigos:
        print("Es valido modificar")

#Empieza El programa

productos = []
personas = []
transacciones = [None] * 20
testigos = []
linkedListTransacciones = listaEnlazadaTransacciones()


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

for x in range(800000):
    producto = {
        "id": x,
        "nombre": "".join([random.choice(string.ascii_lowercase) for x in range(3)]),
        "precio": random.randint(100000, 999999),
        "dueno": (random.choice(personas)).cc
    }
    productos.append(producto)


crearTransaccion(personas, transacciones, productos, 2024, 1, 3)
crearTransaccion(personas, transacciones, productos, 2024, 1, 3)
crearTransaccion(personas, transacciones, productos, 2024, 1, 3)
crearTransaccion(personas, transacciones, productos, 2024, 1, 3)
crearTransaccion(personas, transacciones, productos, 2024, 1, 3)
crearTransaccion(personas, transacciones, productos, 2024, 1, 3)
crearTransaccion(personas, transacciones, productos, 2024, 1, 3)
crearTransaccion(personas, transacciones, productos, 2024, 1, 3)

print("Menu")
print("1. ver transacciones")
print("2. intentar modificar transaccion")
while(True):
    try:
        opcion = int(input("Digite la opcion: "))
    except ValueError:
        print("No valido")
    if opcion not in [1,2]:
        print("No valido")
    else:
        break
if opcion == 1:
    imprimir_transacciones(transacciones)
elif opcion == 2:
    modificarTransaccionRandom(transacciones, testigos)
