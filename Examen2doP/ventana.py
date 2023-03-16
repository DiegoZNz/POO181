import tkinter as tk
from logica import *

class Win(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Examen 2do P matricula")
        self.geometry("700x700")
        
        #Parte de Nombre
        self.nombrelbl = tk.Label(text="Ingresa tu nombre:")
        self.nombrelbl.pack()
        
        self.nombreentry = tk.Entry(self)
        self.nombreentry.pack()
        
        #Parte del ap Paterno
        
        self.apellidoPlbl = tk.Label(text="Ingresa tu Apellido Paterno:")
        self.apellidoPlbl.pack()
      
        self.apellidoPentry = tk.Entry(self)
        self.apellidoPentry.pack()
        
        #Parte del ap Materno
        
        self.apellidoMlbl = tk.Label(text="Ingresa tu Apellido Materno:")
        self.apellidoMlbl.pack()
        
        self.apellidoMentry = tk.Entry(self)
        self.apellidoMentry.pack()
        
        
        
        #Parte de año de nacimiento
        self.añolbl = tk.Label(text="Ingresa tu año de nacimiento:")
        self.añolbl.pack()
        
        self.añoentry = tk.Entry(self)
        self.añoentry.insert(0, "0")
        self.añoentry.pack()
        
        #Parte de la carrera
        
        self.Carreralbl = tk.Label(text="Ingresa carrera:")
        self.Carreralbl.pack()
        
        self.Carreraentry = tk.Entry(self)
        self.Carreraentry.pack()
        
        self.botongenerar = tk.Button(text="Generar Matricula", command=self.Generar)
        self.botongenerar.pack()
        
        
        
        
    def Generar(self):
        GN=diego(self.nombreentry.get(),self.apellidoPentry.get(),self.apellidoMentry.get(),int(self.añoentry.get()),self.Carreraentry.get())
        GN.generarMat() 
        

Ven = Win()
Ven.mainloop()