
import tkinter as tk
from view.frame import Frame1
from view.frame2 import Frame2
from model.insert import Insert
from view.main_menu import Menu
from tests.test import Test_code


insert = Insert()#Despues de ejectutar por primera vez el driver debes comentar la funcion de abajo para que no te de error
#insert.insert_rows()#Comentame despues de ejectutar por primera vez -_-

test = Test_code()
test.test_search_by_name()
test.test_search_by_price()
test.test_search_by_location()
test.test_search_by_range()
test.test_all_products()

root = tk.Tk()
root.title("Plan Pa'Nacho")

root.iconbitmap('img/icon.ico')

menu = Menu()

menu.menu(root)

frame1 = Frame1(root)
frame2 = Frame2(root)

root.mainloop()