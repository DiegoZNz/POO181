import tkinter as tk
from tkinter import ttk
from tkinter import *
from ControladorBD import * #1. Presentamos los archivos XD

#2. Crear un objeto de la clase controiador 
controlador = ControladorBD()   #Nombre del objeto con la clase+

#3. Botonnnn
def EjecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())


Ventana= Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("500x300")

panel=ttk.Notebook (Ventana)
panel.pack(fill='both', expand='yes')
pestana1=ttk.Frame (panel)
pestana2=ttk.Frame (panel)
pestana3=ttk.Frame (panel)
pestana4=ttk. Frame(panel)


# Pestaña 1: Formulario de Usuarios 

Titulo=Label(pestana1,text="Registro de usuarios", fg="blue",font="modern").pack()

varNom= tk.StringVar()
lblNom= Label(pestana1, text= "Nombre: ").pack()
txtNom= Entry (pestana1, textvariable=varNom) .pack()
varCor= tk.StringVar()
lblCor= Label (pestana1, text= "Correo: ").pack()
txtCor= Entry(pestana1, textvariable=varCor).pack()
varCon=tk.StringVar()
lblCon= Label (pestana1, text= "Contraseña: ").pack()
txtNom= Entry(pestana1, textvariable=varCon) .pack()

btnGuardar=Button(pestana1,text='Guardar Usuario',command=EjecutaInsert).pack()

panel.add (pestana1, text='Formulario usuarios')
panel.add (pestana2, text='Buscar Usuario')
panel.add (pestana3, text='Consultar usuarios')
panel.add (pestana4, text='Actualizar usuario')


Ventana.mainloop()
