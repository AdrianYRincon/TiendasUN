from .connection import Data_base
from .table import Table

class Insert:

   def insert_rows(self):


        connection = Data_base()

        table = Table()

        table.create_table()


        products =[('esfero',4000,'La 45'),
       ('cartuchera',25000,"La 45"),
       ('libro',22000,'La 45'),
       ('planillero',15000,'La 45'),
       ('agenda pequeña',9000,'La 45'),
       ('resaltador',10000,'La 45'),
       ('tijeras',8000,'La 45'),
       ('llavero',13000,'La 45'),
       ('dona',2500,'La 45'),
       ('dona mini',2000,'La 45'),
       ('eclair',2600,'La 45'),
       ('gomitas',300,'La 45'),
       ('chocolatina',12000,'La 45'),
       ('mango',2500,'La 45'),
       ('alfajor',3200,'Plaza Che'),
       ('empanada vegana',2000,'Plaza Che'),
       ('hamburguesa vegana',9000,'Plaza Che'),
       ('postres',1200,'Plaza Che'),
       ('pin metalico',10000,'Plaza Che'),
       ('acrilico',5000,'Plaza Che'),
       ('botones',2000,'Plaza Che'),
       ('parches',1000,'Plaza Che'),
       ('arepa boyacense y agua panela',3000,'Plaza Che'),
       ('separador',5000,'Plaza Che'),
       ('mango',600,'Plaza Che'),
       ('banano',800,'Plaza Che'),
       ('caja frambuesas',8500,'Plaza Che'),
       ('manzana',2000,'Plaza Che'),
       ('porcion de fruta',2000,'Plaza Che'),
       ('hamburguesa sencilla',7000,'Plaza Che'),
       ('hamburguesa especial',8000,'Plaza Che'),
       ('hamburguesa super sencilla',5000,'Plaza Che'),
       ('helado',7000,'Plaza Che'),
       ('empanada',2500,'Plaza Che'),
       ('arepa de huevo',2500,'Plaza Che'),
       ('arroz con pollo',8500,'Plaza Che'),
       ('arroz especial',8500,'Plaza Che'),
       ('sandwich',6000,'Plaza Che'),
       ('perro caliente',10000,'Plaza Che'),
       ('tamal',7000,'Plaza Che'),
       ('oblea',2000,'Plaza Che'),
       ('caja esferos',13000,'Plaza Che'),
       ('empanada de carne',2500,'Plaza Che'),
       ('jugo',2000,'Plaza Che'),
       ('postres',2500,'Plaza Che'),
       ('sandwich',6000,'Plaza Che'),
       ('cafe organico',700,'Plaza Che'),
       ('sticker',500,'Plaza Che'),
       ('placa',65000,'Plaza Che'),
       ('parche',15000,'Plaza Che'),
       ('caja parches',85000,'Plaza Che'),
       ('calca',3200,'Plaza Che'),
       ('pin',6000,'Plaza Che'),
       ('postre',4000,'Plaza Che'),
       ('pan de la abuela',2500,'Plaza Che'),
       ('trillador',4000,'Plaza Che'),
       ('pipa',2000,'Plaza Che'),
       ('manilla',2000,'Plaza Che'),
       ('fuchi',5000,'Plaza Che'),
       ('cuarzo',8000,'Plaza Che'),
       ('pomada cannabis',8000,'Plaza Che'),
       ('copa menstrual',4800,'Plaza Che'),
       ('Zumo de Naranja',2000,'Plaza Che'),
       ('vaso de frutas',1500,'Plaza Che'),
       ('empanada de carne',2300,'Plaza Che'),
       ('empanada de pollo',2300,'Plaza Che'),
       ('galleta integral',1000,'Plaza Che'),
       ('oblea',2000,'Plaza Che'),
       ('vaso de yogur',2500,'Plaza Che'),
       ('yogur con granola',1500,'Plaza Che'),
       ('tarrito rojo',500,'Plaza Che'),
       ('miel',500,'Plaza Che'),
       ('turron de mani',1000,'Plaza Che'),
       ('barra de cereal',1200,'Plaza Che'),
       ('pancho',4500,'Plaza Che'),
       ('pancho especial',6000,'Plaza Che'),
       ('panchote',6500,'Plaza Che'),
       ('panchote supremo',8500,'Plaza Che'),
       ('waffle cuadrado',4000,'Plaza Che'),
       ('waffle cuadrado mejorado',5000,'Plaza Che'),
       ('waffle redondo',6000,'Plaza Che'),
       ('empanada',3000,'CYT'),
       ('pastel',3500,'CYT'),
       ('papa rellena',3500,'CYT'),
       ('cuaderno pequeño',3000,'CYT'),
       ('cuaderno argollado',4000,'CYT'),
       ('cuaderno cinco materias',20000,'CYT'),
       ('protoboard',8500,'CYT'),
       ('guantes',4000,'CYT'),
       ('esfero',1000,'CYT'),
       ('pinza',7000,'CYT'),
       ('corta frios',7000,'CYT'),
       ('pelacable',10000,'CYT'),
       ('hoja examen',200,'CYT'),
       ('lapiz',1000,'CYT'),
       ('borrador',800,'CYT'),
       ('perro caliente',4500,'CYT'),
       ('jugo',2000,'CYT'),
       ('arepa de huevo',3000,'CYT'),
       ('pastel de yuca',3000,'CYT'),
       ('postre maracuya',3500,'CYT'),
       ('postre limon',3500,'CYT'),
       ('postre cafe',3500,'CYT'),
       ('postre chocolate',3500,'CYT'),
       ('postre coco',3500,'CYT'),
       ('postre oreo',4000,'CYT'),
       ('pastel de pollo',2500,'CYT'),
       ('pastel de carne',2500,'CYT'),
       ('pasabocas',1000,'CYT'),
       ('repollitas',1000,'CYT'),
       ('pastel y bebida',3000,'CYT')]

        sql = "INSERT INTO products VALUES(null,?,?,?)"

        connection.cursor.executemany(sql,products)

        connection.close()


   def insert_row(self,name,price,location):

      connection = Data_base()

      sql = f"""INSERT INTO products(name,price,location)
    VALUES('{name}','{price}','{location}')"""

      connection.cursor.execute(sql)

      connection.close()


   def delete_row(self,id_product):

      connection = Data_base()

      sql = f"DELETE FROM products WHERE id = {id_product}"

      connection.cursor.execute(sql)

      connection.close()

