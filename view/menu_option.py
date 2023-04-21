from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import Label


class WindowContactus(tk.Toplevel):

    def __init__(self, root = None):
        super().__init__(root)
        self.title("Contactanos")
        self.geometry("370x250")
        self.Window_Contactus()
        self.style = ttk.Style()
        self.entry = ttk.Entry()


    def Window_Contactus(self):

        self.Label1=Label(self, text="Contactanos:",font='Calibri 20 bold')
        self.Label1.config(bg='white',font=('Calibri', 18))
        self.Label1.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.Label2=Label(self, text="Si deseas contactarnos, envianos un mensaje al siguiente correo:")
        self.Label2.config(anchor="w")
        self.Label2.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.Label3=Label(self, text="planpanacho@gmail.com")
        self.Label3.config(fg="blue",font=('Calibri', 14),anchor="w")
        self.Label3.grid(row=4, column=0, sticky="w", padx=10, pady=10)
        self.Label4=Label(self, text="con el asunto: 'reclamo', 'sugerencia' o 'duda'")
        self.Label4.config(anchor="w")
        self.Label4.grid(row=6, column=0, sticky="w", padx=10, pady=10)
        self.button_close = ttk.Button(
            self,
            text="Cerrar ventana",
            command=self.destroy
        )
        self.button_close.place(x=265, y=210)
        self.focus()
        self.grab_set()
      


class LogWindow(tk.Toplevel):

    def __init__(self, root = None):
        super().__init__(root)
        self.title("Herramientas")
        self.geometry("720x300")
        self.Log_Window()

    def Log_Window(self):

            self.Label1=Label(self, text="Registro:",font='Calibri 20 bold')
            self.Label1.config(bg='white',font=('Calibri', 18))
            self.Label1.grid(row=0, column=0, sticky="w", padx=10, pady=10)
            self.Label2=Label(self, text="si deseas registrarte para poder agregar tus producto, estos son los pasos:")
            self.Label2.config(anchor="w")
            self.Label2.grid(row=2, column=0, sticky="w", padx=10, pady=10)
            self.Label3=Label(self, text="1. Envianos un correo con el asunto 'Registro' a 'planpanacho@gmail.com'.")
            self.Label3.config(anchor="w")
            self.Label3.grid(row=3, column=0, sticky="w", padx=10, pady=10)
            self.Label4=Label(self, text="el correo debe contener: comprobante de que es parte de la comunidad unal, (preferiblemente carnet con fotografia) \n comprobante de que realmente tiene una chaza o negocio en la universidad (foto con la chaza)")
            self.Label4.config(anchor="w")
            self.Label4.grid(row=4, column=0, sticky="w", padx=10, pady=10)
            self.Label5=Label(self, text="2. una vez verifiquemos los comprobantes, te enviaremos un usuario y contraseña para que pueda agregar o eliminar productos.")
            self.Label5.config(anchor="w")
            self.Label5.grid(row=5, column=0, sticky="w", padx=10, pady=10)
            self.button_close = ttk.Button(
                self,
                text="Cerrar ventana",
                command=self.destroy
            )
            self.button_close.place(x=595, y=267)
            self.focus()
            self.grab_set()

class WindowAdd(tk.Toplevel):

    def __init__(self, root = None):
        super().__init__(root)
        self.title("Como agregar Productos")
        self.geometry("390x320")
        self.Window_Add()
    
    def Window_Add(self):
            self.Label1=Label(self, text="¿Cómo agregar productos?",font='Calibri 20 bold')
            self.Label1.config(bg='white',font=('Calibri', 18))
            self.Label1.grid(row=0, column=0, sticky="w", padx=10, pady=10)
            self.Label2=Label(self, text="Paso 1. Ingresa con usuario y contraseña.")
            self.Label2.config(anchor="w")
            self.Label2.grid(row=2, column=0, sticky="w", padx=10, pady=10)
            self.Label3=Label(self, text="Paso 2. Ingresa el nombre del producto.")
            self.Label3.config(anchor="w")
            self.Label3.grid(row=3, column=0, sticky="w", padx=10, pady=10)
            self.Label4=Label(self, text="Paso 3. Ingresa el precio del producto sin puntos o comas.")
            self.Label4.config(anchor="w")
            self.Label4.grid(row=4, column=0, sticky="w", padx=10, pady=10)
            self.Label5=Label(self, text="Paso 4. Ingresa la zona en que se puede encontrar el producto.")
            self.Label5.config(anchor="w")
            self.Label5.grid(row=5, column=0, sticky="w", padx=10, pady=10)
            self.Label6=Label(self, text="(conoce las localizaciones en 'Ayuda'->'cuales son las localizaciones'")
            self.Label6.config(anchor="w")
            self.Label6.grid(row=6, column=0, sticky="w", padx=10, pady=10)
            self.Label7=Label(self, text="Paso 5. Presiona el boton 'Agregar'.")
            self.Label7.config(anchor="w")
            self.Label7.grid(row=7, column=0, sticky="w", padx=10, pady=10)
            self.button_close = ttk.Button(
                self,
                text="Cerrar ventana",
                command=self.destroy
            )
            self.button_close.place(x=295, y=285)
            self.focus()
            self.grab_set()

class WindowDelete(tk.Toplevel):

    def __init__(self, root = None):
        super().__init__(root)
        self.title("Eliminar Productos")
        self.geometry("390x320")
        self.Window_Delete()

    def Window_Delete(self):
            self.Label1=Label(self, text="¿Cómo eliminar productos?",font='Calibri 20 bold')
            self.Label1.config(bg='white',font=('Calibri', 18))
            self.Label1.grid(row=0, column=0, sticky="w", padx=10, pady=10)
            self.Label2=Label(self, text="Paso 1. Ingresa con usuario y contraseña.")
            self.Label2.config(anchor="w")
            self.Label2.grid(row=2, column=0, sticky="w", padx=10, pady=10)
            self.Label3=Label(self, text="Paso 2. Ingresa el nombre del producto.")
            self.Label3.config(anchor="w")
            self.Label3.grid(row=3, column=0, sticky="w", padx=10, pady=10)
            self.Label4=Label(self, text="Paso 3. Ingresa el precio del producto sin puntos o comas.")
            self.Label4.config(anchor="w")
            self.Label4.grid(row=4, column=0, sticky="w", padx=10, pady=10)
            self.Label5=Label(self, text="Paso 4. Ingresa la zona en que se puede encontrar el producto.")
            self.Label5.config(anchor="w")
            self.Label5.grid(row=5, column=0, sticky="w", padx=10, pady=10)
            self.Label6=Label(self, text="(conoce las localizaciones en 'Ayuda'->'cuales son las localizaciones'")
            self.Label6.config(anchor="w")
            self.Label6.grid(row=6, column=0, sticky="w", padx=10, pady=10)
            self.Label7=Label(self, text="Paso 5. Presiona el boton 'Eliminar'.")
            self.Label7.config(anchor="w")
            self.Label7.grid(row=7, column=0, sticky="w", padx=10, pady=10)
            self.button_close = ttk.Button(
                self,
                text="Cerrar ventana",
                command=self.destroy
            )
            self.button_close.place(x=295, y=285)
            self.focus()
            self.grab_set()

class WindowImage(tk.Toplevel):

    def __init__(self, root = None):
        super().__init__(root)
        self.title("Mapa locaciones UN")
        self.geometry("550x250")
        
    
    def Window_img(self):
        img = PhotoImage(file="img/mapa un.png")
        self.widget = Label(self, image=img).place(x=0,y=0)
         
        self.button_close = ttk.Button(
                self,
                text="Cerrar ventana",
                command=self.destroy
            )
        self.button_close.place(x=458, y=0)
        self.focus()
        self.grab_set()
        self.mainloop()

class WindowLocation(tk.Toplevel):

    def __init__(self, root = None):
        super().__init__(root)
        self.title("cuales son las localizaciones")
        self.geometry("550x250")
        self.Window_Location()
    
    def img(self):
        self.img= WindowImage(self)
        self.img.Window_img()
        

    def Window_Location(self):
        self.Label1=Label(self, text="¿Cuáles son las localizaciones?",font='Calibri 20 bold')
        self.Label1.config(bg='white',font=('Calibri', 18))
        self.Label1.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.Label2=Label(self, text="las localizaciones en las que puedes enocontrar los productos son las siguientes:")
        self.Label2.config(anchor="w")
        self.Label2.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.Label3=Label(self, text="1. La 45: Recorrido desde el 'Auditorio León de Greiff', hasta la salida por la carrera 30 o calle 45.")
        self.Label3.config(anchor="w")
        self.Label3.grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.Label4=Label(self, text="2. Plaza Che: hace referencia a las chazas alrededor de la Plaza Che.")
        self.Label4.config(anchor="w")
        self.Label4.grid(row=4, column=0, sticky="w", padx=10, pady=10)
        self.Label5=Label(self, text="3. CYT: Recorrido desde el edificio 401 'El Viejo', hasta el edificio 454 'CYT'.")
        self.Label5.config(anchor="w")
        self.Label5.grid(row=5, column=0, sticky="w", padx=10, pady=10)
        self.button_close = ttk.Button(
                self,
                text="Cerrar ventana",
                command=self.destroy
            )
        self.button_close.place(x=455, y=217)
        self.button_img = ttk.Button(self,text="Ver mapa",command=self.img)
        self.button_img.config(padding=10)
        self.button_img.place(x=450,y=10)
        self.focus()
        self.grab_set()