import sqlite3 as sql

class Data_base:

    def __init__(self):

        #Creamos la base de datos o nos conectamos a una base de datps
        self.database = sql.connect('resources/products.db')

        #Creamos el cursor
        self.cursor = self.database.cursor()

    def close(self):

        #Confirmamos los cambios realizados
        self.database.commit()

        #Cerramos la base de datos
        self.database.close()






    

        