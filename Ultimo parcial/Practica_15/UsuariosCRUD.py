import tkinter as tk
from tkinter import ttk
from tkinter import *
from ControladorBD import * #1. Presentamos los archivos XD

#2. Crear un objeto de la clase controiador 
controlador = ControladorBD()   #Nombre del objeto con la clase+

#3. Boton insertar
def EjecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())
#4. Btn consulta
def EjecutaConsult():
    usuario = controlador.consultarUsuario(varBus.get())
    for usu in usuario:
        cadena = str(usu[0])+" " +usu[1] +" " +usu[2] +" " +str(usu[3])
    # Insertar el texto en el widget Text
    if usuario:
        textEnc.delete("1.0", tk.END)
        textEnc.insert(tk.END,cadena) 
    else:
        textEnc.delete("1.0", tk.END)
        messagebox.showinfo("Not found","No se encontro")      
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


# Pestaña 2: Buscar Usuario
TituloSch=Label(pestana2,text="Buscar Usuario", fg="blue",font=("modern",18)).pack()


varBus= tk.StringVar()
lblId= Label(pestana2, text= "Identificador Usuario: ").pack()
txtId= Entry (pestana2, textvariable=varBus) .pack()
btnSch=Button(pestana2,text='Buscar',command=EjecutaConsult).pack()
SubSch=Label(pestana2,text="Encontrado", fg="blue",font=("modern",15)).pack()
textEnc = Text(pestana2, height=5,width=52)
textEnc.pack()

panel.add (pestana1, text='Formulario usuarios')
panel.add (pestana2, text='Buscar Usuario')
panel.add (pestana3, text='Consultar usuarios')
panel.add (pestana4, text='Actualizar usuario')

Ventana.mainloop()
