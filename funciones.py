
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
    nombre = str(input('Ingrese el nombre del producto: '))
    stock = int(input('Ingrese la cantidad stock: '))
    precio = float(input('Ingrese el precio el producto: '))
    sql = f"INSERT INTO  productos (nombre, stock, precio) VALUES ('{nombre}',{stock},{precio})"
    puntero.execute(sql)
    conexion.commit()
def read(puntero,conexion):

    pass

def update(puntero,conexion):

    pass

def delete(puntero, conexion):
    
    pass