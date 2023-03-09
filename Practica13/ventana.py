import tkinter as tk
from logica import *

class Ventana(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Practica 13: AutoPassword")
        self.geometry("600x400")
        
        #Etiqueta de longitud
        self.lenlabel = tk.Label(text="Longitud de la contraseña:")
        self.lenlabel.pack()
        
        #Entry de Longitud
        self.entryLen = tk.Entry(self)
        self.entryLen.pack()
        
        #Checkbox de Mayusculas


        # Crea la casilla de verificación y asocia su estado con la variable "estado"
        self.estado = tk.BooleanVar()
        
        self.estado1 = tk.BooleanVar()
        self.checkboxm = tk.Checkbutton(self, text="Incluir mayuscula",variable=self.estado,onvalue=True, offvalue=False)
        self.checkboxm.pack()
        self.checkboxes = tk.Checkbutton(self, text="Incluir caracteres especiales",variable=self.estado1,onvalue=True, offvalue=False)
        self.checkboxes.pack()
        

        
        #Checkbox de caracteres especiales
        
        
    
        #Boton de ingresar con la funcion de obtener los datos de los entry's, y mandarlos a la clase login
        self.button = tk.Button(self, text="Generar Contraseña", command=self.on_button)
        self.button.pack()
        
    #Función para el botón
    def on_button(self):
        #se crea el objeto con los gets de los entry's
        seg=diego(self.entryLen.get(),self.estado.get(),self.estado1.get())
        #se mandan los parametros de los gets para la funcion loginveriicacion de la clase login.py
        seg.checarSeguridad(int(self.entryLen.get()))
        gen=diego(self.entryLen.get(),self.estado.get(),self.estado1.get())
        gen.generarContraseña(int(self.entryLen.get()),self.estado.get(),self.estado1.get())
        print(self.entryLen.get())
        print(self.estado.get())
        print(self.estado1.get())

ventana = Ventana()
ventana.mainloop()