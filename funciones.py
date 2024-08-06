import os
import time
import msvcrt
from tabulate import tabulate

HEADERS_PROD = ["codgio", "nombre", "tamaño", "categoria", "stock", "precio"]
CENTER_PROD = (("center",)*6)
HEADERS_VENTA = ["cod venta", "producto", "tamaño", "cantidad", "precio", "fecha"]
CENTER_VENTA = (("center",)*6)

def menu():
    '''
        Mostrar menu del programa.

        Muestra las opciones del programa, pide al usuario
        que ingrese la opcion y retorna la opcion
    '''
    print("---------------------Menu del Sistema--------------------")
    print("\t\t\t 1 - Agregar Productos")
    print("\t\t\t 2 - Mostrar Productos")
    print("\t\t\t 3 - Actualizar Productos")
    print("\t\t\t 4 - Eliminar Productos")
    print("\t\t\t 5 - Agregar Categoria")
    print("\t\t\t 6 - Ingresar Ventas De Productos")
    print("\t\t\t 7 - Ver Venta Total Productos")
    print("\t\t\t 8 - Salir Del Gestor")
    opcion = int(input('Ingrese la opcion que desea: '))
    return opcion

def clean_screen(segundo):
    '''
        Limpia la pantalla del sistema.
        
        :param segundo: int segundos

        Del modulo time usamos el metodo sleep() pasando
        como parametro la variable segundo, indicando 
        cuantos segundos esperara el sistema para continuar 
        su ejecucion. Del modulo os usamos el metodo system()
        pasando como parametro la variable 'cls' que es un comando
        de windows para limpiar la pantalla.
    '''
    time.sleep(segundo)
    os.system("cls")

def ver_cat(puntero):
    '''
        Muestra la categoria del producto.

        :param puntero: object - Cursor en Mysql

        Muestra el codigo y el nombre de todas
        las categorias en la base de datos.

    '''
    sql = "select idcat, nombre from categorias"
    head = ["cod categoria", "categoria"]
    center = (("center",)*2)
    read_puntero(puntero,sql,head,center)

'''CATEGORIAS'''

def create_cat(puntero,conexion):
    nombre = str(input('Ingrese el nombre de la nueva categoria: ')).lower()
    sql = f"""insert into categorias (nombre) values ('{nombre}')"""
    puntero.execute(sql)
    conexion.commit()
    print(f'Categoria crreda exitosamente!!!')

''' CRUD DE LOS PRODUCTOS'''

def create(puntero, conexion):
    '''
        Crea un un nuevo producto en la base de datos.

        :param puntero: object MYSQLCursor.
        :param conexion: object MYSQLConnection.

        Esta funcion pide las caracteristicas del producto,
        al nombre y al tamaño del producto lo convierte en minusculas.
        En la variable local sql se define la consulta a la base de datos, 
        con el metodo execute() del objeto puntero se ejecuta la consulta, 
        con el metodo commit() del objeto conexion se guardan los cambios.
    '''
    nombre = str(input('Ingrese el nombre del producto: ')).lower()
    size = str(input('Ingrese el tamaño del producto: ')).lower()
    stock = int(input('Ingrese la cantidad stock: '))
    precio = float(input('Ingrese el precio el producto: '))
    ver_cat(puntero)
    cat = int(input('Ingrese el numero de la categoria del producto: '))
    sql = f"""insert into  productos (nombre, tamaño, idcat, stock,
    precio) values ('{nombre}', '{size}', {cat}, {stock}, {precio})"""
    puntero.execute(sql)
    conexion.commit()

def read_puntero(puntero, sql, headers, center):
    puntero.execute(sql)
    try:
        print(tabulate(puntero, headers=headers, tablefmt="fancy_grid", colalign=center))
    except:
        print(f'No hay ventas registradas!!')


def opcion_prod():
    print("1 - Ver todos los prodcutos")
    print("2 - Ver un producto en especifico")
    opcion = int(input('Ingrese la opcion deseada: '))
    return opcion

def read(puntero):
    opcion = opcion_prod()
    clean_screen(1)
    match opcion:
        case 1:
            sql = f"""select a.idprod, a.nombre, a.tamaño, b.nombre as categoria, a.stock, a.precio 
            from productos a inner join categorias b on a.idcat = b.idcat """
            read_puntero(puntero, sql, HEADERS_PROD, CENTER_PROD)
            print(f'Presione cualquier tecla cuando desee continuear...')
            msvcrt.getch()
            os.system("cls")
        case 2:
            while True:
                producto = int(input('Ingrese el id del producto: '))
                if verificar_producto(puntero, producto) == True:
                    sql = f"""select idprod,a.nombre,tamaño,b.nombre as categoria,stock,precio 
                    from productos a inner join categorias b on a.idcat = b.idcat 
                    where idprod = {producto}"""
                    read_puntero(puntero, sql, HEADERS_PROD, CENTER_PROD)
                    pregunta = str(input('Desea ver otro producto? "s" para si/"n" para no: ')).lower()
                    if pregunta == 'n':
                        clean_screen(1)
                        break
                    clean_screen(2)
                else:
                    print(f'!!El producto no existe, intente de nuevo!!')
                    clean_screen(2)

def verificar_producto(puntero, id):
    '''
        Verifica si un producto esta en la tabla productos.

        :param producto: str - Nombre del producto
        :param puntero: object - Cursor en Mysql
        :return: bool

        Esta funcion ejecuta la consulta de la variable sql
        con el metodo execute() del objeto puntero devolviendo
        una lista de tuplas con los datos de la tabla.
        Con la estructura "for i in puntero" el indice i
        va iterando por las tuplas en la lista, con
        "for j in i" accedemos al valor de cada tupla.
        Luego se verifica si el producto ingresado esta
        en la tupla que se esta iterando, si se encuentra
        se suma 1 a la variable aux y se rompe el for.
        Fuera de la estructura for se verificamos si
        aux es igual a 1, de serlo retorna True, de lo
        contrario retorna False.
    '''
    sql = f"select idprod from productos"
    puntero.execute(sql)
    aux = 0
    for i in puntero:
        for j in i:
            if id == j:
                aux += 1
    if aux == 1:
        return True
    else:
        return False

def update(puntero, conexion):
    '''
        Actualiza la tabla productos.

        :param puntero: object - Cursor en Mysql.
        :param conexion: object - Conexion a Mysql.

        Se ingresa el nombre del producto como string, con el
        metodo lower() se convierte el string en minusculas.
        Con el metodo verificar_producto() verificamos si
        el producto ingresado se encuentra en la tabla productos.

        Si el producto esta en la tabla, con el metodo opcion_update()
        se muestran las opciones de actualizacion. Se ingresa la opcion
        y con la estructura match se analisa la opcion ingresada y se
        determina que accion seguir.

        El metodo commit() del objeto conexion sirve para guardar los
        datos actualizados en la base de datos.
    '''
    while True:
        id = int(input('Ingrese el id del producto que actualizara: '))
        if verificar_producto(puntero, id) == True:
            clean_screen(1)
            opcion = opcion_update()
            clean_screen(1)
            match opcion:
                case 1:
                    stock = get_stock(puntero, id)
                    new_stock = int(input(f'Su stock actual es: {stock}, ingrese la cantidad que agregara: ')) + stock
                    update_file(puntero, conexion, id, "stock", new_stock)
                case 2:
                    precio = float(input('Ingrese el nuevo Precio: '))
                    update_file(puntero, conexion, id, "precio", precio)
                case 3:
                    tamaño = str(input('Ingrese el tamaño del prodcuto: '))
                    sql = f"update productos set tamaño = '{tamaño}' where idprod = {id}"
                    puntero.execute(sql)
                    conexion.commit()
                case 4:
                    nombre = str(input('Ingrese el nuevo nombre del producto: ')).lower()
                    sql = f"update productos set nombre = '{nombre}' where idprod = {id}"
                    puntero.execute(sql)
                    conexion.commit()
                case 5:
                    ver_cat(puntero)
                    categoria = int(input('Ingrese el numero de la categoria: '))
                    update_file(puntero, conexion, id, "idcat", categoria)
                case 6:
                    nombre = str(input('Ingrese el nombre del producto: '))
                    tamaño = str(input('Ingrese el tamaño del prodcuto: '))
                    categoria = int(input('Ingrese el numero de la categoria: '))
                    stock = get_stock(puntero, id)
                    new_stock = int(input(f'Su stock actual es: {stock}, ingrese la cantidad que agregara: ')) + stock
                    precio = float(input('Ingrese el nuevo Precio: '))
                    sql = f"""update productos set nombre = '{nombre}',tamaño = '{tamaño}',idcat = {categoria},
                    stock = {new_stock}, precio = {precio} where idprod = {id}"""
                    puntero.execute(sql)
                    conexion.commit()
            print("¡¡¡El producto se actualizo correctamente!!!")
            pregunta = str(input('Desea actualizar otro producto? "s/n": ')).lower()
            if pregunta == "n":
                clean_screen(1)
                break
            clean_screen(1)
        else:
            print(f'¡¡¡El producto no se encontro. Intente de nuevo...!!!')
            clean_screen(2)

def update_file(puntero, conexion, id, columna, valor):
    sql = f"update productos set {columna} = {valor} where idprod = {id}"
    puntero.execute(sql)
    conexion.commit()

def get_stock(puntero, id):
    sql = f"select stock from productos where idprod = {id}"
    puntero.execute(sql)
    for i in puntero:
        for j in i:
            return j

def opcion_update():
    '''
        Muestra las opciones de actualizacion de productos.

        Muestras las opciones de actualizacion, se ingresa
        la opcion deseada y se retorna la opcion deseada.
    '''
    print("Opciones de actualizacion: ")
    print("1 - Actualizar stock")
    print("2 - Actualizar precio")
    print("3 - Actualizar tamaño")
    print("4 - Actualizar nombre")
    print("5 - Actualizar categoria")
    print("6 - Actualizar todo")
    opcion = int(input('Ingrese el numero de su opcion: '))
    return opcion

def lista_prod(puntero, producto):
    sql = f"select * from productos where idprod = '{producto}'"
    read_puntero(puntero, sql, HEADERS_PROD, CENTER_PROD)

def delete(puntero, conexion):
    while True:
        id = str(input('Ingrese el id del producto: '))
        if verificar_producto(puntero, id) == True:
            sql = f"delete from productos where idprod = '{id}'"
            pregunta = str(input('Esta seguro de eliminar este producto? "s/n": ')).lower()
            if pregunta == "s":
                puntero.execute(sql)
                conexion.commit()
                print(f'¡¡¡El producto fue borrado con exito!!!')
                clean_screen(1)
            if pregunta == "n":
                clean_screen(1)
                break
            pregunta = str(input('Desea eliminar otro producto? "s/n": '))
            if pregunta == "n":
                clean_screen(1)
                break
            clean_screen(1)
        else:
            print(f'No se encontro el producto. Intentelo de nuevo...!!!')
            clean_screen(1)

'''CRUD DE LAS VENTAS'''

def add_venta(puntero, conexion,fecha, en_venta):
    while True:
        id = int(input('Ingrese el id del producto: '))
        if verificar_producto(puntero, id) == True:
            break
        else:
            print(f'No se encontro el producto. Intentelo de nuevo...!!!')
            clean_screen(2)
    cantidad = float(input('Ingrese la cantidad del producto: '))
    precio = get_precio(puntero, id, cantidad)
    clean_screen(1)
    print("\t\tPRODUCTOS")
    tabla_venta(puntero, id, precio, cantidad, en_venta)
    sql = f"insert into ventas (idprodu, cantidad, precio, fecha) values ({id}, {cantidad}, {precio}, '{fecha}')"
    puntero.execute(sql)
    conexion.commit()
    stock = get_stock(puntero, id) - cantidad
    if stock <= 15:
        print(f'\t\t¡¡ALTERTA DE STOCK!!\n Quedan {stock} unidades!!')
    update_file(puntero, conexion, id, "stock", stock)
    return precio

def tabla_venta(puntero, id, precio,cantidad, en_venta):
    sql = f"select idprod, nombre, tamaño from productos where idprod = {id}"
    puntero.execute(sql)
    for i in puntero:
        i = list(i)
        en_venta.append(i)
    en_venta[-1].append(cantidad)
    en_venta[-1].append(precio)
    headers = ["codigo", "nombre", "tamaño", "cantidad", "precio"] 
    center = (("center",)*5)
    print(tabulate(en_venta, headers=headers, tablefmt="fancy_grid", colalign=center))

def get_precio(puntero, id, cantidad):
    sql = f"select precio from productos where idprod = '{id}'"
    puntero.execute(sql)
    for i in puntero:
        for j in i:
            cantidad = j * cantidad
    return cantidad

def verificar_mes():
    while True:
        mes = int(input('Ingrese el numero del mes: '))
        if 0 < mes < 10:
            mes = "0" + str(mes)
            break
        if mes > 12 or mes < 1:
            print('Mes invalido, por favor ingrese un mes entre 1 y 12')
            clean_screen(2)
    mes = str(mes)
    return mes

def opcion_venta():
    print(f'1 - Ventas de todos los productos')
    print('2 - Ventas de un producto especifico')
    opcion = int(input('Ingrese la opcion: '))
    return opcion

def show_precio(puntero):
    for i in puntero:
        for j in i: 
            precio = j
    return precio
