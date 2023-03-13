from tkinter import messagebox

class diego:
    cuentas = {}
    def __init__(self, NCuenta,tit,ed,sal):
        self.__numeroC=NCuenta
        self.__titular=tit
        self.__edad=ed
        self.__saldo=sal
        
    def CrearCuentas(self,NC,Name,edd,sald):
        if NC==0 or Name=='' or edd==0:
            messagebox.showerror("Algo salió mal","Llene todos los campos")
        elif NC in self.cuentas:
            messagebox.showerror("Algo salió mal","Ya existe la cuenta")
        else:
            self.cuentas[NC] = {"titular": Name, "edad": edd, "saldo": sald}
            messagebox.showinfo("Bien","La cuenta se agrego correctamente")
    
    def consultar_saldo(self,NC):
        if NC in self.cuentas:
            messagebox.showinfo("Bien","El saldo de la cuenta {} es: ${}".format(NC, self.cuentas[NC]["saldo"]))
        else:
            messagebox.showerror("error","La cuenta {} no existe.".format(NC))
    
    
    def ingresar_efectivo(self, NC, cantidad):
        if NC in self.cuentas:
            self.cuentas[NC]["saldo"] += cantidad
            self.consultar_saldo(NC)
        else:
            messagebox.showerror("error","La cuenta {} no existe.".format(NC))
    
    def retirar_efectivo(self, NC, cantidad):
        if NC in self.cuentas:
            if self.cuentas[NC]["saldo"]>= cantidad:
                self.cuentas[NC]["saldo"] -= cantidad
                self.consultar_saldo(NC)
            elif self.cuentas[NC]["saldo"]==0:
                messagebox.showerror("Error saldo","Su saldo es de 0")
            else:
                messagebox.showerror("Error saldo","Saldo insuficiente")
        else:
            messagebox.showerror("error","La cuenta {} no existe.".format(NC))
    
    def depositar(self,NC,NCD,cantidad):
        if NC in self.cuentas:
            if NCD in self.cuentas:
                if self.cuentas[NC]["saldo"]>= cantidad:
                    self.cuentas[NC]["saldo"] -= cantidad
                    self.cuentas[NCD]["saldo"]+= cantidad
                    messagebox.showinfo("Exito","Se ha depositado ${} de la cuenta {} a la cuenta {}.".format(cantidad, NC, NCD))
                    self.consultar_saldo(NC)
                    self.consultar_saldo(NCD)
                else:
                    messagebox.showerror("Error saldo","Saldo insuficiente")
            else:
                messagebox.showerror("error","La cuenta {} no existe.".format(NC))
        else:
            messagebox.showerror("error","Su cuenta {} no existe.".format(NC))
        

              
       

