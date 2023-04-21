import tkinter as tk
from .menu_option import *

class Menu:

    def Window_Contactus(self):
        self.Window_Contactus = WindowContactus()

    def Log_Window(self):
        self.Log_Window = LogWindow()
    
    def Window_Add(self):
        self.Window_Add = WindowAdd()

    def Window_Delete(self):
        self.Window_Delete = WindowDelete()

    def Window_Location(self):
        self.Window_Location = WindowLocation()

    def menu(self,root):

        #Creamos un barra de menu
        bar_menu = tk.Menu(root)
        #metemos en la raiz la barra de menu con su tamaño
        root.config(menu=bar_menu, width=300, heigh=300,bg='skyblue3')

        #Creamos el menu cascada de inicio y quitamos la linea que sale por defecto
        menu_inicio =tk.Menu(bar_menu, tearoff=0)
        #Creamos el menu cascada de configuración
        menu_informacion =tk.Menu(bar_menu, tearoff=0)
        #Creamos el menu cascada de ayuda
        menu_ayuda =tk.Menu(bar_menu, tearoff=0)

        #Creamos un menu cascada y lo llamanos inicio
        bar_menu.add_cascade(label= 'Inicio', menu= menu_inicio)
        bar_menu.add_cascade(label= 'Informacion', menu= menu_informacion)
        bar_menu.add_cascade(label= 'Ayuda', menu= menu_ayuda)

        #
        menu_inicio.add_command(label='Salir', command= root.destroy)

        #Creamos los labels que van dentro de la barra de menu configurar
        menu_informacion.add_command(label='Contactanos',command=self.Window_Contactus)
        menu_informacion.add_command(label= 'Registro',command=self.Log_Window)

        #Creamos los labels que van dentro de la barra de menu ayuda
        menu_ayuda.add_command(label='como agregar productos?',command=self.Window_Add)
        menu_ayuda.add_command(label= 'como eliminar productos?',command=self.Window_Delete) 
        menu_ayuda.add_command(label='cuales son las localizaciones?',command=self.Window_Location)

