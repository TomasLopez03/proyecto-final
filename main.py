import mysql.connector 
from funciones import *
#conectar a la base de datos hospital
conexion = mysql.connector.connect(
    user = "root",
    password = "azurro03",
    host = "localhost",
    database = "negocio"
)
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
# puntero.execute("select * from productos")
# for i in puntero: 
#     print(i)
