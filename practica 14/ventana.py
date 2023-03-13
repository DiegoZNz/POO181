import tkinter as tk 
from logica import *

class Win(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Practica 14: Administración")
        self.geometry("500x700")
        self.lblNCuenta = tk.Label(text="No. Cuenta:")
        self.lblNCuenta.pack()
    
        #Entry de No. Cuenta
        self.entryNCuenta = tk.Entry(self,justify='center')
        self.entryNCuenta.insert(0, "0")
        self.entryNCuenta.pack()
        
        #Etiqueta de titular
        self.lbltitular = tk.Label(text="Titular:")
        self.lbltitular.pack()
    
        #Entry de No. Cuenta
        self.entrytitular = tk.Entry(self,justify='center')
        self.entrytitular.pack()
        
        #Etiqueta de edad
        self.lbledad = tk.Label(text="Edad:")
        self.lbledad.pack()
    
        #Entry de No. Cuenta
        self.entryedad = tk.Entry(self,justify='center')
        self.entryedad.insert(0, "0")
        self.entryedad.pack()
        
        #Etiqueta de saldo
        self.lblsaldo = tk.Label(text="SALDO:")
        self.lblsaldo.pack()
    
        #Entry de saldo
        self.entrysaldo = tk.Entry(self,justify='center')
        self.entrysaldo.insert(0, "0")
        self.entrysaldo.pack()

        #Boton
        self.buttonCS = tk.Button(self, text="Agregar Clientes", bg="#008080", fg="#FFFFFF",font=("Helvetica", 15), command=self.on_button)
        self.buttonCS.pack()
        
        #Entry de NC
        self.lblNC = tk.Label(text="Numero de cuenta:")
        self.lblNC.pack()
        self.entryefectivor = tk.Entry(self,justify='center')
        self.entryefectivor.insert(0, "0")
        self.entryefectivor.pack()
        
        self.buttonCK = tk.Button(self, text="Verificar Saldo", bg="#008080", fg="#FFFFFF",font=("Helvetica", 15), command=self.cheq)
        self.buttonCK.pack()
        
        #*******************************************Ingresar********************************
        self.lblNC2 = tk.Label(text="Numero de cuenta:")
        self.lblNC2.pack()
        self.entryNC22 = tk.Entry(self,justify='center')
        self.entryNC22.insert(0, "0")
        self.entryNC22.pack()
        self.lblmonto = tk.Label(text="Monto a depositar:")
        self.lblmonto.pack()
        self.entrymonto = tk.Entry(self,justify='center')
        self.entrymonto.insert(0, "0")
        self.entrymonto.pack()
        
        self.buttonCKc = tk.Button(self, text="Ingresar efectivo", bg="#008080", fg="#FFFFFF",font=("Helvetica", 15), command=self.cash)
        self.buttonCKc.pack()
        
        #*******************************************Retirar********************************
        self.lblNC3 = tk.Label(text="Numero de cuenta:")
        self.lblNC3.pack()
        self.entryNC3 = tk.Entry(self,justify='center')
        self.entryNC3.insert(0, "0")
        self.entryNC3.pack()
        self.lblmonto2 = tk.Label(text="Monto a retirar:")
        self.lblmonto2.pack()
        self.entrymonto2 = tk.Entry(self,justify='center')
        self.entrymonto2.insert(0, "0")
        self.entrymonto2.pack()
        
        self.buttonCKr = tk.Button(self, text="Retirar efectivo", bg="#008080", fg="#FFFFFF",font=("Helvetica", 15), command=self.ret)
        self.buttonCKr.pack()
        #*******************************************Depositar********************************
        self.lblNC4 = tk.Label(text="Tú número de cuenta:")
        self.lblNC4.pack()
        self.entryNC4 = tk.Entry(self,justify='center')
        self.entryNC4.insert(0, "0")
        self.entryNC4.pack()
        self.lblNC5 = tk.Label(text="Numero de cuenta a depositar:")
        self.lblNC5.pack()
        self.entryNC5 = tk.Entry(self,justify='center')
        self.entryNC5.insert(0, "0")
        self.entryNC5.pack()
        self.lblmonto3 = tk.Label(text="Monto a retirar:")
        self.lblmonto3.pack()
        self.entrymonto3 = tk.Entry(self,justify='center')
        self.entrymonto3.insert(0, "0")
        self.entrymonto3.pack()
        
        self.buttonCKd = tk.Button(self, text="Depositar", bg="#008080", fg="#FFFFFF",font=("Helvetica", 15), command=self.dep)
        self.buttonCKd.pack()
        
    #apartado de Funciones de botones    
    def on_button(self):
        CSTR=diego(int(self.entryNCuenta.get()),self.entrytitular.get(),int(self.entryedad.get()),float(self.entrysaldo.get()))
        CSTR.CrearCuentas(int(self.entryNCuenta.get()),self.entrytitular.get(),int(self.entryedad.get()),float(self.entrysaldo.get()))
        self.entryNCuenta.delete(0, tk.END)
        self.entryNCuenta.insert(0, "0")
        self.entrytitular.delete(0, tk.END)
        self.entryedad.delete(0, tk.END)
        self.entryedad.insert(0, "0")
        self.entrysaldo.delete(0, tk.END)
        self.entrysaldo.insert(0, "0")
        
    def cheq(self):
        CSTR=diego(any,any,any,any)
        CSTR.consultar_saldo(int(self.entryefectivor.get()))
    
    def cash(self):
        CSTR=diego(any,any,any,any)
        CSTR.ingresar_efectivo(int(self.entryNC22.get()),float(self.entrymonto.get()))
        
    def ret(self):
        CSTR=diego(any,any,any,any)
        CSTR.retirar_efectivo(int(self.entryNC3.get()),float(self.entrymonto2.get()))
        
    def dep(self):
        CSTR=diego(any,any,any,any)
        CSTR.depositar(int(self.entryNC4.get()),int(self.entryNC5.get()),float(self.entrymonto3.get()))
        
        
ventana = Win()
ventana.mainloop()