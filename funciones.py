
def menu():
    print("---------------------Bienvenidos a su Gestor de Datos--------------------")
    print("\t\t\t 1 - Agregar Productos")
    print("\t\t\t 2 - Mostrar Productos")
    print("\t\t\t 3 - Actualizar Productos")
    print("\t\t\t 4 - Eliminar Productos")
    print("\t\t\t 5 - Ingresar Ventas De Productos")
    print("\t\t\t 6 - Ver Venta Total Productos")
    print("\t\t\t 7 - Ver Venta De Un Producto")
    print("\t\t\t 8 - Salir Del Gestor")

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
            verificar = verificar_producto(producto, puntero)
            print(f"verificar funciones.py: {verificar}")

            if verificar == True:
                sql =  f"select nombre, stock, precio from productos where nombre like '%{producto}%' "
                read_puntero(puntero, sql)

   # return verificar

def verificar_producto(producto, puntero):
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


# def update(puntero, conexion):
#     pass

# def delete(puntero, conexion):
#     pass