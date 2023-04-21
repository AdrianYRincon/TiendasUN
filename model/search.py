from .connection import Data_base

class Search:


    def all_products(self):

        connection = Data_base()

        sql  = """SELECT * FROM products"""

        list = []

        

        connection.cursor.execute(sql)


        list = connection.cursor.fetchall()


        connection.close()

        return list
        
        


    def search_by_location(self,location):

        connection = Data_base()

        sql = f"""SELECT * FROM products WHERE location = '{location}'"""  


        connection.cursor.execute(sql)


        datos = connection.cursor.fetchall()


        connection.close()

        return datos
        
        


       


    def search_by_price(self,price):

        connection = Data_base()

        sql = f"""SELECT * FROM products WHERE price = {price}"""  


        connection.cursor.execute(sql)


        datos = connection.cursor.fetchall()


        connection.close()

        return datos

        


       

    def search_by_name(self,name):

        connection = Data_base()

        sql = f"""SELECT * FROM products WHERE name = '{name}'"""  

        connection.cursor.execute(sql)

        datos = connection.cursor.fetchall()

        connection.close()


        return datos

        

    def search_by_range(self,price):

        connection = Data_base()

        sql = f"""SELECT * FROM products WHERE price <= {price}"""  


        connection.cursor.execute(sql)


        datos = connection.cursor.fetchall()


        connection.close()

        return datos

        
