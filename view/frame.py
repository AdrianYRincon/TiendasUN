import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from model.insert import Insert
from model.search import Search



class Frame1(tk.Frame):
    
    def __init__(self, root = None):

        super().__init__(root)
        self.root = root
        self.config(width=320,height=380,bg='lightsteelblue3')
        self.grid(column=0,row=0,columnspan=4)

        self.style = ttk.Style(self)

       

        self.label()
        self.entry()
        self.button()
        self.option_menu()
        self.table()

       

    def label(self):


        self.label_name = tk.Label(self,text='Buscar producto por:')
        self.label_name.config(bg='lightsteelblue3',font=('Arial', 12),fg='black')
        self.label_name.grid(row = 0, column=0, padx=10,pady= 10)




    def selection(self,selected):

       
        if selected=='Nombre producto':

            self.button_search.config(command=self.search_name,bg='royalblue4')

        elif selected=='Precio':

            self.button_search.config(command=self.search_price,bg='royalblue4')

        elif selected=='Ubicación':

            self.button_search.config(command=self.search_location,bg='royalblue4')
        elif selected=='Maximo valor':

            self.button_search.config(command=self.search_range,bg='royalblue4')


            

    
    def option_menu(self):


        self.option_value = tk.StringVar()

        self.option_value.set('Seleccione')

        self.options = ['Nombre producto','Precio','Ubicación','Maximo valor']

        self.menu = tk.OptionMenu(self,self.option_value,*self.options,command=self.selection)

        self.menu.config(width=20,cursor='hand2',bg='royalblue4',fg='white')

        self.menu.grid(row = 0, column=1, padx=10,pady= 10)



    def entry(self):

        self.info = tk.StringVar()
        self.entry_search = tk.Entry(self, textvariable=self.info)
        self.entry_search.config(width=50)
        self.entry_search.grid(row = 0, column=2, padx=10,pady= 10)

    def button(self):
 

        self.button_search = tk.Button(self,text='Buscar')
        self.button_search.config(width=20,cursor='hand2',command=self.no_option,bg='royalblue4',fg='white')
        self.button_search.grid(row=0,column=3)
        


    def table(self):



        self.table_products = ttk.Treeview(self,column=('Nombre','Precio','Ubicación'))
        self.table_products.grid(row=2,pady=10,padx=5, column=0, columnspan=4, sticky='nse')
        self.table_products.config(height=13)


        #Scrollbar para los productos
        self.scroll = ttk.Scrollbar(self,orient='vertical', command=self.table_products.yview)
        self.scroll.grid(row=2,column=4, sticky='nse')
        self.table_products.configure(yscrollcommand= self.scroll.set)  

        self.table_products.heading('#0', text='ID')
        self.table_products.heading('#1', text='NOMBRE PRODUCTO')
        self.table_products.heading('#2', text='PRECIO')
        self.table_products.heading('#3', text='UBICACIÓN')

        
        products = Search()
        list = products.all_products() 
        list.reverse()


        for product in list:

            self.table_products.insert('',0,text=product[0],
            values=(product[1],product[2],product[3]))

 


    def search_name(self):



        name_product = self.info.get()
        
        if name_product=='':

            titulo = 'Buscar por nombre'
            mensaje = 'Ingresa el nombre del producto'
            messagebox.showinfo(titulo,mensaje)

        else:

            search = Search()

            list = search.search_by_name(name_product)

            list.reverse()
            
            self.table_products.delete(*self.table_products.get_children())

        

            for product in list:

                self.table_products.insert('',0,text=product[0],
                values=(product[1],product[2],product[3]))


           


        
    def search_price(self):


        try:
            price_product = self.info.get()

            if price_product=='':
                titulo = 'Buscar por precio'
                mensaje = 'Ingresa un precio'
                messagebox.showinfo(titulo,mensaje)

            else:

                search = Search()

                list = search.search_by_price(price_product)

                list.reverse()
                
                self.table_products.delete(*self.table_products.get_children())

            

                for product in list:

                    self.table_products.insert('',0,text=product[0],
                    values=(product[1],product[2],product[3]))

        except:
            titulo = 'Buscar por precio'
            mensaje = 'Ingresa un precio válido'
            messagebox.showwarning(titulo,mensaje)
            



    def search_location(self):

        location_product = self.info.get()
        
         
        if location_product=='':

            titulo = 'Buscar por ubicación'
            mensaje = 'Ingresa la ubicación en donde deseas buscar'
            messagebox.showinfo(titulo,mensaje)
    
        else:
                
            search = Search()

            list = search.search_by_location(location_product)

            list.reverse()
            
            self.table_products.delete(*self.table_products.get_children())

        

            for product in list:

                self.table_products.insert('',0,text=product[0],
                values=(product[1],product[2],product[3]))


    def search_range(self):


        try:

            price_range = self.info.get()

            if price_range=='':

                titulo = 'Buscar por máximo precio'
                mensaje = 'Ingresa el máximo precio de los productos que quieres ver'
                messagebox.showinfo(titulo,mensaje)

            else:

                search = Search()

                list = search.search_by_range(price_range)

                list.reverse()
                
                self.table_products.delete(*self.table_products.get_children())

                

                for product in list:

                    self.table_products.insert('',0,text=product[0],
                    values=(product[1],product[2],product[3]))

        except:
            titulo = 'Buscar por máximo'
            mensaje = 'Ingresa un precio válido'
            messagebox.showwarning(titulo,mensaje)

    def no_option(self):

        if self.option_value.get()=='Seleccione':
                titulo = 'Seleccionar'
                mensaje = 'Selecciona una opción para buscar'
                messagebox.showinfo(titulo,mensaje)

       
      
      
    def delete_product(self):

        
        try:

            delete = Insert()

            

            self.id_product = self.table_products.item(self.table_products.selection())['text']



            delete.delete_row(self.id_product)

            self.table()

        except:

            titulo = 'Eliminar producto'
            mensaje = 'Escoge el producto que deseas eliminar'
            messagebox.showinfo(titulo,mensaje)



