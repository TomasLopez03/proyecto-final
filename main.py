import mysql.connector #libreria para conectarse con mysql
from datetime import datetime #librearia para utilizar fechas
import msvcrt #libreria para interactuar en tiempo de ejecutcion
from funciones import * #libreria propia

#Defino conexion como un objeto MYSQLConnection
conexion = mysql.connector.connect(
    user = "root",
    password = "azurro03",
    host = "localhost",
    database = "negocio"
)

#Defino puntero como un objeto MYSQLCursor
puntero = conexion.cursor()

while True: 
    '''mostrando menu'''
    opcion = menu()
    clean_screen(1)
    match opcion: 
        case 1: 
            '''agregar productos'''
            create(puntero, conexion)
            print(f'¡¡¡Producto agregado con exito!!!')
            clean_screen(1)
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
            '''Agregar Categoria'''
            create_cat(puntero, conexion)
            clean_screen(2)
        case 6:
            '''Agregar Ventas'''
            aux = 0
            en_venta = []
            while True:
                tiempo = datetime.now()
                fecha = tiempo.strftime("%Y-%m-%d")
                aux += add_venta(puntero, conexion, fecha, en_venta)
                op = str(input('Ingresara otro producto? "s" para si/ "n" para no: ')).lower()
                if op == "n":
                    clean_screen(1)
                    print(f'El total de la compra es: ${aux}')
                    print(f'Presione cualquier tecla cuando desee continuear...')
                    msvcrt.getch()
                    clean_screen(1)
                    break
                clean_screen(1)
        case 7: 
            opcion = opcion_venta()
            clean_screen(1)
            match opcion:
                case 1: 
                    año = str(input('Ingrese el año: '))
                    mes = verificar_mes()
                    sql = f"""select idventas, nombre, tamaño , cantidad, a.precio, fecha 
                    from ventas a inner join productos b on a.idprodu = b.idprod 
                    where fecha like '{año}-{mes}%'"""
                    read_puntero(puntero, sql, HEADERS_VENTA, CENTER_VENTA)
                    sql = f"select sum(precio) from ventas where fecha like '{año}-{mes}%'"
                    puntero.execute(sql)
                    precio = show_precio(puntero)
                    if precio is not None:
                        print(f'El total de las ventas del mes es: ${precio}')
                    print(f'Presione cualquier tecla cuando desee continuear...')
                    msvcrt.getch()
                    clean_screen(1)
                case 2:
                    id = int(input('Ingrese el id del producto: '))
                    año = str(input('Ingrese el año: '))
                    mes = verificar_mes()
                    sql = f"""select idventas, nombre, tamaño, cantidad, a.precio, fecha 
                    from ventas a inner join productos b on a.idprodu = b.idprod 
                    where a.idprodu = {id} and fecha like '{año}-{mes}%'"""
                    read_puntero(puntero, sql, HEADERS_VENTA, CENTER_VENTA)
                    sql = f"""select sum(a.precio) from ventas a 
                    inner join productos b on a.idprodu = b.idprod 
                    where a.idprodu = {id} and fecha like '{año}-{mes}%'"""
                    puntero.execute(sql)
                    precio = show_precio(puntero)
                    if precio is not None:
                        print(f'El total de las ventas en el mes es de: ${precio}')
                    print(f'Presione cualquier tecla cuando desee continuear...')
                    msvcrt.getch()
                    clean_screen(1)
        case 8:
            print("¡¡¡Esta saliendo del programa!!!")
            clean_screen(2)
            break
