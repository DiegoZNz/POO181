from tkinter import messagebox
import random

class diego:
    def __init__(self,nom,app,apm,añn,añc,carr):
        self.__nombre=nom
        self.__apellidoP=app
        self.__apellidoM=apm
        self.__añoNacimiento=añn
        self.__añoEnCurso=añc
        self.__carrera=carr
        
    def generarMat(self):
        if self.__nombre=='' or self.__apellidoP=='' or self.__apellidoM=='' or self.__añoNacimiento==0 or self.__añoEnCurso==0 or self.__carrera =='':
            messagebox.showerror("error", "Por favor rellena todos los datos")
        else:
            Nombre=self.__nombre[0]
            APP=self.__apellidoP[:2]
            APM=self.__apellidoM[:2]
            Año=str(self.__añoNacimiento)[-2:]
            añc=str(self.__añoEnCurso)[-2:]
            car=self.__carrera[:3]
            rand1=random.randint(0,9)
            rand2=random.randint(0,9)
            Matricula=Nombre+APP+APM+str(Año)+añc+car+str(rand1)+str(rand2)
            messagebox.showinfo("Matricula", Matricula)
            
        