print("--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("		57.BBDD_III_2 ")
print("--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
# -------------------------------------------------------------
import sqlite3
# -------------------------------------------------------------
miConexion=sqlite3.connect("57.GestionProductos")

miCursor=miConexion.cursor()

# -------------------------------------------------------------
miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','Tren',15,'Jugueteria')")
# -------------------------------------------------------------
miConexion.commit()
# -------------------------------------------------------------
miConexion.close()
# -------------------------------------------------------------
