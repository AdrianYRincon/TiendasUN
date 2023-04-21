import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Style
from model.insert import Insert
from .frame import Frame1


class Frame2(tk.Frame):

    def __init__(self, root = None):

        super().__init__(root,width=350,height=350)
        self.root = root
        self.config(bg='skyblue3')
        self.grid(column=4,row=0,columnspan=1)

        self.user = tk.StringVar()
        self.password = tk.StringVar()

        self.style = ttk.Style(self)

        self.style.theme_use('xpnative')

        self.label_products()
        self.info_admin()
        self.entry_products()
        self.disable_fields()
        
        

    def info_admin(self):


        self.label_user = tk.Label(self,text='Usuario:')
        self.label_user.config(padx=10,pady=10)
        self.label_user.config(bg='skyblue3',font=('Arial', 10),fg="black",anchor="w",width=8)
        self.label_user.grid(column=0,row=1,sticky='se')

        self.label_password = tk.Label(self,text='Contraseña:')
        self.label_password.config(padx=10,pady=10)
        self.label_password.config(bg='skyblue3',font=('Arial', 10),fg="black",anchor="w",width=8)
        self.label_password.grid(column=0,row=2,sticky='se')
        
        self.entry_user = tk.Entry(self,textvariable=self.user)
        self.entry_user.grid(row=1, column=1, padx=10,pady=10,sticky='sw')
        self.entry_user.config(width=40)

        
        self.entry_password = tk.Entry(self, textvariable=self.password)
        self.entry_password.grid(row =2, column=1, padx=10,pady=10,sticky='sw')
        self.entry_password.config(width=40,show='*')

        self.button_confirm = tk.Button(self,text='Confirmar',command=self.user_check)
        self.button_confirm.config(width=15,cursor='hand2',fg="white",bg='royalblue4')
        self.button_confirm.grid(row=3,column=1)


    def label_products(self):

        self.label_title = tk.Label(self,text='¡Agrega tus productos!',font='Calibri 20 bold')
        self.label_title.config(bg='skyblue3',fg="white",anchor="n")
        self.label_title.config(padx=10,pady=10)
        self.label_title.grid(column=0,row=0,columnspan=2)


        self.label_name = tk.Label(self,text='Nombre:')
        self.label_name.config(bg='skyblue3',font=('Arial', 10),fg="black",anchor="w",width=8)
        self.label_name.config(padx=10,pady=10)
        self.label_name.grid(column=0,row=5,sticky='se')

        self.label_price = tk.Label(self,text='Precio:')
        self.label_price.config(bg='skyblue3',font=('Arial', 10),fg="black",anchor="w",width=8)
        self.label_price.config(padx=10,pady=10)
        self.label_price.grid(column=0,row=6,sticky='se')

        self.label_location = tk.Label(self,text='Ubicación:')
        self.label_location.config(bg='skyblue3',font=('Arial', 10),fg="black",anchor="w",width=8)
        self.label_location.config(padx=10,pady=10)
        self.label_location.grid(column=0,row=7,sticky='se')
        

        
    def entry_products(self):

        self.product = tk.StringVar()
        self.entry_product = tk.Entry(self,textvariable=self.product)
        self.entry_product.grid(row =5, column=1, padx=10,pady=10,sticky='sw')
        self.entry_product.config(width=40)

        self.price = tk.StringVar()
        self.entry_price = tk.Entry(self, textvariable=self.price)
        self.entry_price.grid(row =6, column=1, padx=10,pady=10,sticky='sw')
        self.entry_price.config(width=40)

        self.location = tk.StringVar()
        self.entry_location = tk.Entry(self,textvariable=self.location)
        self.entry_location.grid(row=7,column=1,padx=10,pady=10,sticky='sw')
        self.entry_location.config(width=40)

        self.button_add = tk.Button(self,text='Agregar')
        self.button_add.config(width=15,cursor='hand2',command=self.add_product,fg="white",bg='royalblue4')
        self.button_add.grid(row=8,column=1,sticky='se',padx=0) 

        self.frame1 = Frame1()
        
        self.button_delete = tk.Button(self,text='Eliminar')
        self.button_delete.config(width=15,cursor='hand2',command=self.frame1.delete_product,fg="white",bg='royalblue4')
        self.button_delete.grid(row=8,column=1,sticky='sw')

    def enable_fields(self):


        self.product.set('')
        self.price.set('')
        self.location.set('')

        self.entry_product.config(state='normal')
        self.entry_price.config(state='normal')
        self.entry_location.config(state='normal')
        self.button_add.config(state='normal')
        self.button_delete.config(state='normal')



    def disable_fields(self):


        self.product.set('')
        self.price.set('')
        self.location.set('')

        self.entry_product.config(state='disabled')
        self.entry_price.config(state='disabled')
        self.entry_location.config(state='disabled')
        self.button_add.config(state='disabled')
        self.button_delete.config(state='disabled')


    def disable_admin(self):

        self.entry_user.config(state='disabled')
        self.entry_password.config(state='disabled')
        self.button_confirm.config(state='disabled')


    def clear_fields(self):

       
        self.product.set('')
        self.price.set('')
        self.location.set('')


    def user_check(self):

        if self.user.get() =='adrian' and self.password.get() =='adrian':

            self.enable_fields()
            self.disable_admin()

        elif self.user.get() =='' and self.password.get() =='':
            
            titulo = 'Datos de usuario'
            mensaje = 'Digite su usuario y contraseña'
            messagebox.showinfo(titulo,mensaje)

        elif self.user.get() =='' and self.password.get() !='':
            
            titulo = 'Datos de usuario'
            mensaje = 'Digite su usuario'
            messagebox.showinfo(titulo,mensaje)

        elif self.user.get() !='' and self.password.get() =='':
            
            titulo = 'Datos de usuario'
            mensaje = 'Digite su contraseña'
            messagebox.showinfo(titulo,mensaje)

        elif self.user.get() !='adrian' and self.password.get() !='adrian':
            
            titulo = 'Datos de usuario'
            mensaje = 'Datos incorrectos,digite de nuevo'
            messagebox.showwarning(titulo,mensaje) 


    def add_product(self):


        if self.product.get()=='' or self.price.get()=='' or self.location.get()=='':
            titulo = 'Agregar producto'
            mensaje = 'Debe rellenar todos los campos'
            messagebox.showinfo(titulo,mensaje)
        
        else:
            insert = Insert()

            insert.insert_row(self.product.get(),self.price.get(),self.location.get())

            self.frame1.table()


            self.clear_fields()



       



        