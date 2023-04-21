from .connection import Data_base

class Table:


    def create_table(self):

        connection = Data_base()

        sql = """CREATE TABLE products(
            id INTEGER, 
            name VARCHAR(60)NOT NULL,
            price DECIMAL(6,2)NOT NULL,
            location VARCHAR(60)NOT NULL,
            PRIMARY KEY(id AUTOINCREMENT)
        )"""


        connection.cursor.execute(sql)
        connection.close()

