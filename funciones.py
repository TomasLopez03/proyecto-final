def menu():
    print("---------------------Menu del Sistema--------------------")
    print("\t\t\t 1 - Agregar Productos")
    print("\t\t\t 2 - Mostrar Productos")
    print("\t\t\t 3 - Actualizar Productos")
    print("\t\t\t 4 - Eliminar Productos")
    print("\t\t\t 5 - Ingresar Ventas De Productos")
    print("\t\t\t 6 - Ver Venta Total Productos")
    print("\t\t\t 7 - Ver Venta De Un Producto")
    print("\t\t\t 8 - Salir Del Gestor")

''' CRUD DE LOS PRODUCTOS'''

def create(puntero, conexion):
    '''
        Crea un registro en la tabla productos.

        :param puntero: object MYSQLCursor.
        :param conexion: object MYSQLConnection.

        Esta funcion pide el nombre, stock, precio del producto
        al contenido de la variable local nombre lo convierte en
        minusculas.
        En la variable local sql se define la query, con el metodo
        execute() del objeto puntero se ejecuta la query, con el
        metodo commit() del objeto conexion se guardan los cambios.
    '''
    nombre = str(input('Ingrese el nombre del producto: ')).lower()
    stock = int(input('Ingrese la cantidad stock: '))
    precio = float(input('Ingrese el precio el producto: '))
    sql = f"insert into  productos (nombre, stock, precio) values ('{nombre}',{stock},{precio})"
    puntero.execute(sql)
    conexion.commit()

def read_puntero(puntero, sql):
    puntero.execute(sql)
    for i in puntero:
        print(i)

def read(puntero):
    opcion = int(input(f"Si vera todos los productos ingrese '1', si vera uno en especifico ingrese '2': "))

    match opcion:
        case 1:
            sql = "select nombre, stock, precio from productos"
            read_puntero(puntero, sql)
        case 2:
            producto = str(input('Ingrese el nombre del producto: ')).lower()
            if verificar_producto(puntero, producto) == True:
                sql = f"select nombre, stock, precio from productos where nombre like '{producto}' "
                read_puntero(puntero, sql)

def verificar_producto(puntero, producto):
    '''
        Verifica si un producto esta en la tabla productos.

        :param producto: str - Nombre del producto
        :param puntero: object - Cursor en Mysql
        :return: bool

        Esta funcion ejecuta la query de la variable sql
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
    sql = "select nombre from productos"
    puntero.execute(sql)
    aux = 0
    for i in puntero:
        for j in i:
            if producto == j:
                aux +=1
                break
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
    producto = str(input('Ingrese el nombre del producto que actualizara: ')).lower()
    if verificar_producto(puntero, producto) == True:
        opcion_update()
        opcion = int(input('Ingrese el numero de su opcion: '))
        ide = get_puntero(puntero, producto)
        match opcion:
            case 1:
                stock = int(input('Ingrese el nuevo Stock: '))
                sql = f"update productos set stock = {stock} where id_productos = {ide}"
                puntero.execute(sql)
                conexion.commit()
            case 2:
                precio = int(input('Ingrese el nuevo Precio: '))
                sql = f"update productos set precio = {precio} where id_productos = {ide}"
                puntero.execute(sql)
                conexion.commit()
            case 3:
                stock = int(input('Ingrese el nuevo Stock: '))
                precio = float(input('Ingrese el nuevo Precio: '))
                sql = f"update productos set stock = {stock}, precio = {precio} where id_productos = {ide}"
                puntero.execute(sql)
                conexion.commit()
        print("¡¡¡El producto se actualizo correctamente!!!")
    else: 
        print(f'¡¡¡El producto no existe!!!')
        
def get_puntero(puntero, producto):
    '''
        Obtiene el valor de la tupla en el puntero.
    '''
    sql = f"select id_productos from productos where nombre = '{producto}'"
    puntero.execute(sql)
    for i in puntero:
        for j in i:
            return j

def opcion_update():
    '''
        Muestra las opciones de actualizacion de productos.
    '''
    print("Opciones de actualizacion: ")
    print("1 - Actualizar stock")
    print("2 - Actualizar precio")
    print("3 - Actualizar stock y precio")

def delete(puntero, conexion):
    producto = str(input('Ingrese el nombre del producto: '))
    if verificar_producto(puntero, producto) == True: 
        sql = f"delete from productos where nombre = '{producto}'"
        puntero.execute(sql)
        conexion.commit()
        print(f'¡¡¡El producto fue borrado con exito!!!')
    else:
        print(f'¡¡¡El producto no existe!!!')

'''CRUD DE LAS VENTAS'''

def add_venta(puntero, conexion):
    producto = str(input('Ingrese el nombre del producto: '))
    id = get_puntero(puntero, producto)
    cantidad = float(input('Ingrese la cantidad del producto: '))
    precio = get_precio(puntero, producto, cantidad)
    sql = f"insert into ventas (id_productos, cantidad, precio) values ({id}, {cantidad}, {precio})"
    puntero.execute(sql)
    conexion.commit() 
    return precio

def get_precio(puntero, producto, cantidad):
    sql = f"select precio from productos where nombre = '{producto}'"
    puntero.execute(sql)
    for i in puntero:
        for j in i:
            aux = j
    aux = aux * cantidad
    return aux
