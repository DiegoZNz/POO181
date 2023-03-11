from tkinter import messagebox
import random
import string

class diego:
    def __init__(self, NCuenta,tit,ed,sal):
        self.__numeroC=NCuenta
        self.__titular=tit
        self.__edad=ed
        self.__saldo=sal
    
    def consultarSaldo(self, NC):
        if NC==self.__numeroC:
            saldo=self.__saldo
            messagebox.showinfo("Consultar saldo",saldo)
            
    def ingresarEfectivo(self,NC,SaldoTot,Cantidad):
        if NC==self.__numeroC:
            SaldoTot=self.__saldo+Cantidad
            messagebox.showinfo("Consultar saldo",SaldoTot)
            return self.__saldo+SaldoTot
    
    def Retirarefectivo(self,NC,SaldoTot,Cantidad):
        if NC==self.__numeroC:
            SaldoTot=self.__saldo
            SaldoTot=SaldoTot-Cantidad
            messagebox.showinfo("Consultar saldo",SaldoTot)
            
            
    def Depositar(self,NC,SaldoTot,Cantidad,NCD):
        if NC==self.__numeroC:
            SaldoTot=SaldoTot-Cantidad
            messagebox.showinfo("Consultar saldo",SaldoTot)
            
        
            
            
            
