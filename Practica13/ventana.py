import tkinter as tk
from logica import *

class Ventana(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Practica 13: AutoPassword")
        self.geometry("400x200")
        
        #Etiqueta de longitud
        self.lenlabel = tk.Label(text="Longitud de la contraseña:")
        self.lenlabel.pack()
        
        #Entry de Longitud
        self.entryLen = tk.Entry(self)
        self.entryLen.insert(0, "8")
        self.entryLen.pack()
        
        
        # Crea la casilla de verificación y asocia su estado con la variable "estado" y creamos los checkbox 
        self.estado = tk.BooleanVar()
        self.estado1 = tk.BooleanVar()
        #Checkbox de Mayusculas
        self.checkboxm = tk.Checkbutton(self, text="Incluir mayuscula",variable=self.estado,onvalue=True, offvalue=False)
        self.checkboxm.pack()
        #Checkbox de caracteres especiales
        self.checkboxes = tk.Checkbutton(self, text="Incluir caracteres especiales",variable=self.estado1,onvalue=True, offvalue=False)
        self.checkboxes.pack()

        #Boton de ingresar con la funcion de obtener la longitud del entry, y mandarlos a la clase logica
        self.button = tk.Button(self, text="Generar Contraseña", bg="#008080", fg="#FFFFFF",font=("Helvetica", 15), command=self.on_button)
        self.button.pack()
        
        #entry de la contraseña generada.
        self.entryCopy = tk.Entry(self)
        self.entryCopy.pack()
        
        
    #Función para el botón
    def on_button(self):
        #se crea el objeto con los gets de los entry's
        seg=diego(self.entryLen.get(),self.estado.get(),self.estado1.get())
        seg.checarSeguridad(int(self.entryLen.get()))
        gen=diego(self.entryLen.get(),self.estado.get(),self.estado1.get())
        
        #aqui esta la función del entry para copiar desde el mismo entry 
        self.entryCopy.delete(0, tk.END)
        self.entryCopy.insert(0,gen.generarContraseña(int(self.entryLen.get()),self.estado.get(),self.estado1.get()) )
        
        
ventana = Ventana()
ventana.mainloop()