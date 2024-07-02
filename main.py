import mysql.connector 
from funciones import *

#Defino conexion como un objeto MYSQLConnection
conexion = mysql.connector.connect(
    user = "root",
    password = "azurro03",
    host = "localhost",
    database = "negocio"
)

#Defino puntero como un objeto MYSQLCursor
puntero = conexion.cursor()

'''
    Programa gestor de ventas.
    Cada producto se guarda como : 
    nombre-cant.vendida-precio.
    Consultas a realizar:
    querys CRUD.
    venta total y por producto.
'''



while True: 
    '''mostrando menu'''
    menu()
    opcion = int(input('Ingrese su opcion: '))
    match opcion: 
        case 1: 
            '''agregar productos'''
            create(puntero, conexion)
            print(f'¡¡¡Producto agregado con exito!!!')
        case 2:
            '''Mostrar productos'''
            read(puntero)
        case 3:
            '''Actualizar producto'''
            update(puntero, conexion)
        case 4: 
            '''Eliminar producto'''
            delete(puntero, conexion)
        case 5:
            aux = 0
            while True:
                aux += add_venta(puntero, conexion)
                op = str(input('Ingresara otro producto? "s" para si/ "n" para no: ')).lower()
                if op == "n":
                    print(f'El total de la compra es: ${aux}')
                    break
        case 6: 
            pass
        case 7:
            pass
        case 8:
            break

#puntero.execute("select nombre from productos;")
# producto = "coca cola"
