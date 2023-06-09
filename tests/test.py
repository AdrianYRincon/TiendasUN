import unittest
from model.search import Search

class Test_code(unittest.TestCase):

    def test_search_by_name(self):
        self.search = Search()
        self.assertEqual(self.search.search_by_name(''),[])
        self.assertEqual(self.search.search_by_name('Libro'),[])
        self.assertEqual(self.search.search_by_name('libro'),[(3, 'libro', 22000, 'La 45')])
        self.assertEqual(self.search.search_by_name('arepa boyacense y agua panela'),[(23,'arepa boyacense y agua panela',3000,'Plaza Che')])



    def test_search_by_price(self):
        self.search = Search()
        self.assertEqual(self.search.search_by_price('250'),[])
        self.assertEqual(self.search.search_by_price('400'),[])
        self.assertEqual(self.search.search_by_price('1000'),[(22, 'parches', 1000, 'Plaza Che'),
        (67, 'galleta integral', 1000, 'Plaza Che'),
        (73, 'turron de mani', 1000, 'Plaza Che'),
        (90, 'esfero', 1000, 'CYT'),
        (95, 'lapiz', 1000, 'CYT'),
        (109, 'pasabocas', 1000, 'CYT'),
        (110, 'repollitas', 1000, 'CYT')])
        self.assertEqual(self.search.search_by_price('5000'),[(20, 'acrilico', 5000, 'Plaza Che'),
        (24, 'separador', 5000, 'Plaza Che'),
        (32, 'hamburguesa super sencilla', 5000, 'Plaza Che'),
        (59, 'fuchi', 5000, 'Plaza Che'),
        (80, 'waffle cuadrado mejorado', 5000, 'Plaza Che')])

    def test_search_by_range(self):
        self.search = Search()
        self.assertEqual(self.search.search_by_range('100'),[])
        self.assertEqual(self.search.search_by_range('200'),[(94, 'hoja examen', 200, 'CYT')])
        self.assertEqual(self.search.search_by_range('500'),[(12, 'gomitas', 300, 'La 45'),
        (48, 'sticker', 500, 'Plaza Che'),
        (71, 'tarrito rojo', 500, 'Plaza Che'),
        (72, 'miel', 500, 'Plaza Che'),
        (94, 'hoja examen', 200, 'CYT')])




    def test_search_by_location(self):
        self.search = Search()
        self.assertEqual(self.search.search_by_location('La'),[])

        self.assertEqual(self.search.search_by_location(''),[])

        self.assertEqual(self.search.search_by_location('123131'),[])

        self.assertEqual(self.search.search_by_location('La 45'),[(1, 'esfero', 4000, 'La 45'),
        (3, 'libro', 22000, 'La 45'),
        (4, 'planillero', 15000, 'La 45'),
        (5, 'agenda pequeña', 9000, 'La 45'),
        (6, 'resaltador', 10000, 'La 45'),
        (7, 'tijeras', 8000, 'La 45'),
        (8, 'llavero', 13000, 'La 45'),
        (9, 'dona', 2500, 'La 45'),
        (10, 'dona mini', 2000, 'La 45'),
        (11, 'eclair', 2600, 'La 45'),
        (12, 'gomitas', 300, 'La 45'),
        (13, 'chocolatina', 12000, 'La 45'),
        (14, 'mango', 2500, 'La 45')])

        self.assertEqual(self.search.search_by_location('Plaza Che'),[ (15,'alfajor',3200,'Plaza Che'),
       (16,'empanada vegana',2000,'Plaza Che'),
       (17,'hamburguesa vegana',9000,'Plaza Che'),
       (18,'postres',1200,'Plaza Che'),
       (19,'pin metalico',10000,'Plaza Che'),
       (20,'acrilico',5000,'Plaza Che'),
       (21,'botones',2000,'Plaza Che'),
       (22,'parches',1000,'Plaza Che'),
       (23,'arepa boyacense y agua panela',3000,'Plaza Che'),
       (24,'separador',5000,'Plaza Che'),
       (25,'mango',600,'Plaza Che'),
       (26,'banano',800,'Plaza Che'),
       (27,'caja frambuesas',8500,'Plaza Che'),
       (28,'manzana',2000,'Plaza Che'),
       (29,'porcion de fruta',2000,'Plaza Che'),
       (30,'hamburguesa sencilla',7000,'Plaza Che'),
       (31,'hamburguesa especial',8000,'Plaza Che'),
       (32,'hamburguesa super sencilla',5000,'Plaza Che'),
       (33,'helado',7000,'Plaza Che'),
       (34,'empanada',2500,'Plaza Che'),
       (35,'arepa de huevo',2500,'Plaza Che'),
       (36,'arroz con pollo',8500,'Plaza Che'),
       (37,'arroz especial',8500,'Plaza Che'),
       (38,'sandwich',6000,'Plaza Che'),
       (39,'perro caliente',10000,'Plaza Che'),
       (40,'tamal',7000,'Plaza Che'),
       (41,'oblea',2000,'Plaza Che'),
       (42,'caja esferos',13000,'Plaza Che'),
       (43,'empanada de carne',2500,'Plaza Che'),
       (44,'jugo',2000,'Plaza Che'),
       (45,'postres',2500,'Plaza Che'),
       (46,'sandwich',6000,'Plaza Che'),
       (47,'cafe organico',700,'Plaza Che'),
       (48,'sticker',500,'Plaza Che'),
       (49,'placa',65000,'Plaza Che'),
       (50,'parche',15000,'Plaza Che'),
       (51,'caja parches',85000,'Plaza Che'),
       (52,'calca',3200,'Plaza Che'),
       (53,'pin',6000,'Plaza Che'),
       (54,'postre',4000,'Plaza Che'),
       (55,'pan de la abuela',2500,'Plaza Che'),
       (56,'trillador',4000,'Plaza Che'),
       (57,'pipa',2000,'Plaza Che'),
       (58,'manilla',2000,'Plaza Che'),
       (59,'fuchi',5000,'Plaza Che'),
       (60,'cuarzo',8000,'Plaza Che'),
       (61,'pomada cannabis',8000,'Plaza Che'),
       (62,'copa menstrual',4800,'Plaza Che'),
       (63,'Zumo de Naranja',2000,'Plaza Che'),
       (64,'vaso de frutas',1500,'Plaza Che'),
       (65,'empanada de carne',2300,'Plaza Che'),
       (66,'empanada de pollo',2300,'Plaza Che'),
       (67,'galleta integral',1000,'Plaza Che'),
       (68,'oblea',2000,'Plaza Che'),
       (69,'vaso de yogur',2500,'Plaza Che'),
       (70,'yogur con granola',1500,'Plaza Che'),
       (71,'tarrito rojo',500,'Plaza Che'),
       (72,'miel',500,'Plaza Che'),
       (73,'turron de mani',1000,'Plaza Che'),
       (74,'barra de cereal',1200,'Plaza Che'),
       (75,'pancho',4500,'Plaza Che'),
       (76,'pancho especial',6000,'Plaza Che'),
       (77,'panchote',6500,'Plaza Che'),
       (78,'panchote supremo',8500,'Plaza Che'),
       (79,'waffle cuadrado',4000,'Plaza Che'),
       (80,'waffle cuadrado mejorado',5000,'Plaza Che'),
       (81,'waffle redondo',6000,'Plaza Che')])

        self.assertEqual(self.search.search_by_location('CYT'),[(82,'empanada',3000,'CYT'),
       (83,'pastel',3500,'CYT'),
       (84,'papa rellena',3500,'CYT'),
       (85,'cuaderno pequeño',3000,'CYT'),
       (86,'cuaderno argollado',4000,'CYT'),
       (87,'cuaderno cinco materias',20000,'CYT'),
       (88,'protoboard',8500,'CYT'),
       (89,'guantes',4000,'CYT'),
       (90,'esfero',1000,'CYT'),
       (91,'pinza',7000,'CYT'),
       (92,'corta frios',7000,'CYT'),
       (93,'pelacable',10000,'CYT'),
       (94,'hoja examen',200,'CYT'),
       (95,'lapiz',1000,'CYT'),
       (96,'borrador',800,'CYT'),
       (97,'perro caliente',4500,'CYT'),
       (98,'jugo',2000,'CYT'),
       (99,'arepa de huevo',3000,'CYT'),
       (100,'pastel de yuca',3000,'CYT'),
       (101,'postre maracuya',3500,'CYT'),
       (102,'postre limon',3500,'CYT'),
       (103,'postre cafe',3500,'CYT'),
       (104,'postre chocolate',3500,'CYT'),
       (105,'postre coco',3500,'CYT'),
       (106,'postre oreo',4000,'CYT'),
       (107,'pastel de pollo',2500,'CYT'),
       (108,'pastel de carne',2500,'CYT'),
       (109,'pasabocas',1000,'CYT'),
       (110,'repollitas',1000,'CYT'),
       (111,'pastel y bebida',3000,'CYT')])
        



    
    def test_all_products(self):
        self.search = Search()
        self.assertEqual(self.search.all_products(),[(1,'esfero',4000,'La 45'),
       (2,'cartuchera',25000,"la 45"),
       (3,'libro',22000,'La 45'),
       (4,'planillero',15000,'La 45'),
       (5,'agenda pequeña',9000,'La 45'),
       (6,'resaltador',10000,'La 45'),
       (7,'tijeras',8000,'La 45'),
       (8,'llavero',13000,'La 45'),
       (9,'dona',2500,'La 45'),
       (10,'dona mini',2000,'La 45'),
       (11,'eclair',2600,'La 45'),
       (12,'gomitas',300,'La 45'),
       (13,'chocolatina',12000,'La 45'),
       (14,'mango',2500,'La 45'),
       (15,'alfajor',3200,'Plaza Che'),
       (16,'empanada vegana',2000,'Plaza Che'),
       (17,'hamburguesa vegana',9000,'Plaza Che'),
       (18,'postres',1200,'Plaza Che'),
       (19,'pin metalico',10000,'Plaza Che'),
       (20,'acrilico',5000,'Plaza Che'),
       (21,'botones',2000,'Plaza Che'),
       (22,'parches',1000,'Plaza Che'),
       (23,'arepa boyacense y agua panela',3000,'Plaza Che'),
       (24,'separador',5000,'Plaza Che'),
       (25,'mango',600,'Plaza Che'),
       (26,'banano',800,'Plaza Che'),
       (27,'caja frambuesas',8500,'Plaza Che'),
       (28,'manzana',2000,'Plaza Che'),
       (29,'porcion de fruta',2000,'Plaza Che'),
       (30,'hamburguesa sencilla',7000,'Plaza Che'),
       (31,'hamburguesa especial',8000,'Plaza Che'),
       (32,'hamburguesa super sencilla',5000,'Plaza Che'),
       (33,'helado',7000,'Plaza Che'),
       (34,'empanada',2500,'Plaza Che'),
       (35,'arepa de huevo',2500,'Plaza Che'),
       (36,'arroz con pollo',8500,'Plaza Che'),
       (37,'arroz especial',8500,'Plaza Che'),
       (38,'sandwich',6000,'Plaza Che'),
       (39,'perro caliente',10000,'Plaza Che'),
       (40,'tamal',7000,'Plaza Che'),
       (41,'oblea',2000,'Plaza Che'),
       (42,'caja esferos',13000,'Plaza Che'),
       (43,'empanada de carne',2500,'Plaza Che'),
       (44,'jugo',2000,'Plaza Che'),
       (45,'postres',2500,'Plaza Che'),
       (46,'sandwich',6000,'Plaza Che'),
       (47,'cafe organico',700,'Plaza Che'),
       (48,'sticker',500,'Plaza Che'),
       (49,'placa',65000,'Plaza Che'),
       (50,'parche',15000,'Plaza Che'),
       (51,'caja parches',85000,'Plaza Che'),
       (52,'calca',3200,'Plaza Che'),
       (53,'pin',6000,'Plaza Che'),
       (54,'postre',4000,'Plaza Che'),
       (55,'pan de la abuela',2500,'Plaza Che'),
       (56,'trillador',4000,'Plaza Che'),
       (57,'pipa',2000,'Plaza Che'),
       (58,'manilla',2000,'Plaza Che'),
       (59,'fuchi',5000,'Plaza Che'),
       (60,'cuarzo',8000,'Plaza Che'),
       (61,'pomada cannabis',8000,'Plaza Che'),
       (62,'copa menstrual',4800,'Plaza Che'),
       (63,'Zumo de Naranja',2000,'Plaza Che'),
       (64,'vaso de frutas',1500,'Plaza Che'),
       (65,'empanada de carne',2300,'Plaza Che'),
       (66,'empanada de pollo',2300,'Plaza Che'),
       (67,'galleta integral',1000,'Plaza Che'),
       (68,'oblea',2000,'Plaza Che'),
       (69,'vaso de yogur',2500,'Plaza Che'),
       (70,'yogur con granola',1500,'Plaza Che'),
       (71,'tarrito rojo',500,'Plaza Che'),
       (72,'miel',500,'Plaza Che'),
       (73,'turron de mani',1000,'Plaza Che'),
       (74,'barra de cereal',1200,'Plaza Che'),
       (75,'pancho',4500,'Plaza Che'),
       (76,'pancho especial',6000,'Plaza Che'),
       (77,'panchote',6500,'Plaza Che'),
       (78,'panchote supremo',8500,'Plaza Che'),
       (79,'waffle cuadrado',4000,'Plaza Che'),
       (80,'waffle cuadrado mejorado',5000,'Plaza Che'),
       (81,'waffle redondo',6000,'Plaza Che'),
       (82,'empanada',3000,'CYT'),
       (83,'pastel',3500,'CYT'),
       (84,'papa rellena',3500,'CYT'),
       (85,'cuaderno pequeño',3000,'CYT'),
       (86,'cuaderno argollado',4000,'CYT'),
       (87,'cuaderno cinco materias',20000,'CYT'),
       (88,'protoboard',8500,'CYT'),
       (89,'guantes',4000,'CYT'),
       (90,'esfero',1000,'CYT'),
       (91,'pinza',7000,'CYT'),
       (92,'corta frios',7000,'CYT'),
       (93,'pelacable',10000,'CYT'),
       (94,'hoja examen',200,'CYT'),
       (95,'lapiz',1000,'CYT'),
       (96,'borrador',800,'CYT'),
       (97,'perro caliente',4500,'CYT'),
       (98,'jugo',2000,'CYT'),
       (99,'arepa de huevo',3000,'CYT'),
       (100,'pastel de yuca',3000,'CYT'),
       (101,'postre maracuya',3500,'CYT'),
       (102,'postre limon',3500,'CYT'),
       (103,'postre cafe',3500,'CYT'),
       (104,'postre chocolate',3500,'CYT'),
       (105,'postre coco',3500,'CYT'),
       (106,'postre oreo',4000,'CYT'),
       (107,'pastel de pollo',2500,'CYT'),
       (108,'pastel de carne',2500,'CYT'),
       (109,'pasabocas',1000,'CYT'),
       (110,'repollitas',1000,'CYT'),
       (111,'pastel y bebida',3000,'CYT')])      
       



