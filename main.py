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



'''mostrando menu'''
#menu()
'''agregar productos'''
# create(puntero, conexion)
#puntero.execute("select nombre from productos;")



verificar = read(puntero)
print(f"verificar main.py: {verificar}")

if  verificar == False:
    print(f'¡¡El producto no se encuentra!!')
