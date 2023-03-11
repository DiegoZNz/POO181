import tkinter as tk
from logica import *

class Ventana(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Practica 14: Administración")
        self.geometry("800x400")

        #Etiqueta de No. Cuenta
        self.lblNCuenta = tk.Label(text="No. Cuenta:")
        self.lblNCuenta.pack()
    
        #Entry de No. Cuenta
        self.entryNCuenta = tk.Entry(self)
        self.entryNCuenta.pack()
        
        #Etiqueta de titular
        self.lbltitular = tk.Label(text="Titular:")
        self.lbltitular.pack()
    
        #Entry de No. Cuenta
        self.entrytitular = tk.Entry(self)
        self.entrytitular.pack()
        
        #Etiqueta de edad
        self.lbledad = tk.Label(text="Edad:")
        self.lbledad.pack()
    
        #Entry de No. Cuenta
        self.entryedad = tk.Entry(self)
        self.entryedad.pack()
        
        #Etiqueta de saldo
        self.lblsaldo = tk.Label(text="SALDO:")
        self.lblsaldo.pack()
    
        #Entry de saldo
        self.entrysaldo = tk.Entry(self)
        self.entrysaldo.pack()

        #Boton
        self.buttonCS = tk.Button(self, text="Consultar saldo", bg="#008080", fg="#FFFFFF",font=("Helvetica", 15), command=self.on_button)
        self.buttonCS.pack()
        
        #Etiqueta de efectivo
        self.lblefectivo = tk.Label(text="Monto a ingresar:")
        self.lblefectivo.pack()
    
        #Entry de saldo
        self.entryefectivo = tk.Entry(self)
        self.entryefectivo.insert(0, "0")
        self.entryefectivo.pack()
        
        self.buttonIE = tk.Button(self, text="Ingresar efectivo", bg="#008080", fg="#FFFFFF",font=("Helvetica", 15), command=self.ingresarEf)
        self.buttonIE.pack()
        
        
        #Etiqueta de efectivo
        self.lblefectivor = tk.Label(text="Monto a retirar:")
        self.lblefectivor.pack()
    
        #Entry de saldo
        self.entryefectivor = tk.Entry(self)
        self.entryefectivor.insert(0, "0")
        self.entryefectivor.pack()
        
        self.buttonre = tk.Button(self, text="retirar efectivo", bg="#008080", fg="#FFFFFF",font=("Helvetica", 15), command=self.retirarEf)
        self.buttonre.pack()
        
        #Etiqueta de cuenta
        self.lblefectivodep = tk.Label(text="Monto a retirar:")
        self.lblefectivodep.pack()
    
        #Entry de saldo
        self.entryefectivodep = tk.Entry(self)
        self.entryefectivodep.insert(0, "0")
        self.entryefectivodep.pack()
        
        self.lblNCD = tk.Label(text="Monto a retirar:")
        self.lblNCD.pack()
    
        #Entry de saldo
        self.entryNCD = tk.Entry(self)
        self.entryNCD.insert(0, "0")
        self.entryNCD.pack()
        
        self.buttonre = tk.Button(self, text="Depositar efectivo", bg="#008080", fg="#FFFFFF",font=("Helvetica", 15), command=self.depositar)
        self.buttonre.pack()
        
        
    #Función para el botón
    def on_button(self):
        #se crea el objeto con los gets de los entry's
        Cuenta=diego(int(self.entryNCuenta.get()),self.entrytitular.get(),int(self.entryedad.get()),float(self.entrysaldo.get()))
        Cuenta.consultarSaldo(int(self.entryNCuenta.get()))
        #gen=diego(self.entryLen.get(),self.estado.get(),self.estado1.get())
        #self.entryCopy.delete(0, tk.END)
        #self.entryCopy.insert(0,gen.generarContraseña(int(self.entryLen.get()),self.estado.get(),self.estado1.get()))
    def ingresarEf(self):
        Ingresar=diego(int(self.entryNCuenta.get()),self.entrytitular.get(),int(self.entryedad.get()),float(self.entrysaldo.get()))
        Ingresar.ingresarEfectivo(int(self.entryNCuenta.get()),float(self.entrysaldo.get()),float(self.entryefectivo.get()))
        
    def retirarEf(self):
        ret=diego(int(self.entryNCuenta.get()),self.entrytitular.get(),int(self.entryedad.get()),float(self.entrysaldo.get()))
        ret.Retirarefectivo(int(self.entryNCuenta.get()),float(self.entrysaldo.get()),float(self.entryefectivor.get()))
    
    
    def depositar(self):
        dep=diego(int(self.entryNCuenta.get()),self.entrytitular.get(),int(self.entryedad.get()),float(self.entrysaldo.get()))
        dep.Depositar(int(self.entryNCuenta.get()),float(self.entrysaldo.get()),float(self.entryefectivor.get()),int(self.entryNCD.get()))     
          
ventana = Ventana()
ventana.mainloop()