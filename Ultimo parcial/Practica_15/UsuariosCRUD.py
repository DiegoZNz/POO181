import tkinter as tk
from tkinter import ttk, font
from tkinter import *
from ControladorBD import * #1. Presentamos los archivos XD

#2. Crear un objeto de la clase controlador 
controlador = ControladorBD()   #Nombre del objeto con la clase

#3. Boton insertar
def EjecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())
    #borra todos los campos cada que se ejecuta el botón
    txtNom.delete("0", "end")
    txtCor.delete("0", "end")
    txtCon.delete("0", "end")
#4. Btn consulta
def EjecutaConsult():
    usuario = controlador.consultarUsuario(varBus.get())
    for usu in usuario:
        cadena = str(usu[0])+" " +usu[1] +" " +usu[2] +" " +str(usu[3])
    # Insertar el texto en el widget Text
    if usuario:
        textEnc.delete("1.0", tk.END)#limpia el texto antes de insertar algo(evita sobrescritura de info)
        textEnc.insert(tk.END,cadena) 
    else:
        textEnc.delete("1.0", tk.END)
        messagebox.showinfo("Not found","No se encontro")    

#5 Función para el botón de actualizar, mostrará los entrys 
def MostrarYSettear():
    #limpiamos los entrys primero que nada
    txtId.delete("0", "end")
    txtNomUP.delete("0", "end")
    txtCorUP.delete("0", "end")
    txtConUP.delete("0", "end")
    # Obtengo el índice del elemento seleccionado
    selected = tree.selection()[0]
    # obtener los valores del elemento seleccionado
    values = tree.item(selected)['values']
    # asignar los valores de Nombre, correo, contraseña(encriptada) a los entry's
    txtId.insert(0, values[0])
    txtNomUP.insert(0, values[1])
    txtCorUP.insert(0, values[2])
    txtConUP.insert(0, values[3])
    #Mandar a la pestaña de actualizar/borrar registros
    panel.select(3)
    
    # mostrar los entry's ocultos (para evitar bugs y errores que los usuarios puedan ocasionar)
    lblInfo.pack_forget()#ocultar la instrucción 
    TituloUP.pack()
    lblNomUP.pack()
    txtNomUP.pack()
    lblCorUP.pack()
    txtCorUP.pack()
    lblConUP.pack()
    txtConUP.pack()
    btnUP.pack()
    btnDlt.pack()
    
    
def EjecutaUpdate():
    #validamos si el controlador.ActualizarUsuario devolvió un valor True se ejecute la consulta y se oculten todos las etiquietas y los entrys, y se limpien.
    if controlador.ActualizarUsuario(varIdUp.get(),varNomUP.get(),varCorUP.get(),varConUP.get()):
        #ocultar lbl y txt
        TituloUP.pack_forget()
        lblNomUP.pack_forget()
        txtNomUP.pack_forget()
        lblCorUP.pack_forget()
        txtCorUP.pack_forget()
        lblConUP.pack_forget()
        txtConUP.pack_forget()
        #limpiar txt
        txtNomUP.delete("0", "end")
        txtCorUP.delete("0", "end")
        txtConUP.delete("0", "end")

        btnUP.pack_forget()
        btnDlt.pack_forget()
        #como se ocultaron las etiquetas y entrys, se muestra la etiqueta de instrucciones
        lblInfo.pack()

    
def EjecutaDelete():
    #validamos si el controlador.EliminarUser devolvió un valor True se ejecute la consulta y se oculten todos las etiquietas y los entrys, y se limpien.
    if controlador.EliminarUser(varIdUp.get()):
        #ocultar lbl y txt
        TituloUP.pack_forget()
        lblNomUP.pack_forget()
        txtNomUP.pack_forget()
        lblCorUP.pack_forget()
        txtCorUP.pack_forget()
        lblConUP.pack_forget()
        txtConUP.pack_forget()
        #limpiar txt
        txtNomUP.delete("0", "end")
        txtCorUP.delete("0", "end")
        txtConUP.delete("0", "end")
        
        btnUP.pack_forget()
        btnDlt.pack_forget()
        #como se ocultaron las etiquetas y entrys, se muestra la etiqueta de instrucciones
        lblInfo.pack()

#######################################################################################################
#Aqui empieza la parte de la interfaz gráfica


Ventana= Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("1000x500")

panel=ttk.Notebook (Ventana)
panel.pack(fill='both', expand='yes')
pestana1=ttk.Frame (panel)
pestana2=ttk.Frame (panel)
pestana3=ttk.Frame (panel)
pestana4=ttk.Frame(panel)

#fuente personalizada
fuente = font.Font(family='Helvetica', size=12, weight='bold')


# Pestaña 1: Formulario de Usuarios 
Titulo=Label(pestana1,text="Registro de usuarios", fg="blue",font=fuente).pack()
varNom= tk.StringVar()
lblNom= Label(pestana1, text= "Nombre: ").pack()
txtNom= Entry (pestana1, textvariable=varNom) 
txtNom.pack()
varCor= tk.StringVar()
lblCor= Label (pestana1, text= "Correo: ").pack()
txtCor= Entry(pestana1, textvariable=varCor)
txtCor.pack()
varCon=tk.StringVar()
lblCon= Label (pestana1, text= "Contraseña: ").pack()
txtCon= Entry(pestana1, textvariable=varCon) 
txtCon.pack()
btnGuardar=Button(pestana1,text='Guardar Usuario',command=EjecutaInsert).pack()


# Pestaña 2: Buscar Usuario
TituloSch=Label(pestana2,text="Buscar Usuario", fg="blue",font=(fuente,18)).pack()
varBus= tk.StringVar()
lblId= Label(pestana2, text= "Identificador Usuario: ").pack()
txtId= Entry (pestana2, textvariable=varBus) .pack()
btnSch=Button(pestana2,text='Buscar',command=EjecutaConsult).pack()
SubSch=Label(pestana2,text="Encontrado", fg="blue",font=(fuente,15)).pack()
textEnc = Text(pestana2, height=5,width=52)
textEnc.pack()


# Pestaña 3: Consultar Usuarios
TituloCons=Label(pestana3,text="Consultar Usuario", fg="blue",font=(fuente,10)).pack()
#Creación del treeview
columns = ('ID','Nombre', 'Correo', 'Contraseña')
tree = ttk.Treeview(pestana3, columns=columns, show='headings')
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Correo", text="Correo")
tree.heading("Contraseña", text="Contraseña")
tree.pack()

#aquí se pondrá el botón para actualizar los registros que se mostraron en el treeview
btnUpdate=Button(pestana3, text='Actualizar',command=MostrarYSettear)
#pero se oculta para que se ejecute solamente cuando se presiona un registro(para evitar bugs y errores por los usuarios)
btnUpdate.pack_forget()


# Pestaña 4: Actualizar Usuarios
TituloUP=Label(pestana4,text="Actualización de datos", fg="blue",font=fuente)
#instrucciones para mostrar la función que está un poco oculta.
lblInfo= Label (pestana4, text= "Por favor diríjase a la sección consultar usuarios y presione sobre el registro que quiera hacer una modificación o eliminación",fg="red",font=fuente)
lblInfo.pack()
varIdUp=tk.StringVar()
txtId= Entry(pestana4, textvariable=varIdUp)
varNomUP= tk.StringVar()
lblNomUP= Label(pestana4, text= "Nombre: ")
txtNomUP= Entry (pestana4, textvariable=varNomUP)
varCorUP= tk.StringVar()
lblCorUP= Label (pestana4, text= "Correo: ")
txtCorUP= Entry(pestana4, textvariable=varCorUP)
varConUP=tk.StringVar()
lblConUP= Label (pestana4, text= "Contraseña: ")
txtConUP= Entry(pestana4, textvariable=varConUP)
btnUP=Button(pestana4,text='Guardar Actualización',command=EjecutaUpdate)
btnDlt=Button(pestana4,text='¡¡¡Eliminar!!!',fg="red",command=EjecutaDelete)

#creamos todos los componentes pero no se muestran porque no les ponemos el .pack() o sea que están "invisibles" y en su lugar ponemos:

#Aqui es una funcion para ocultar las etiquetas y los entry's con el .pack_forget()
TituloUP.pack_forget()
lblNomUP.pack_forget()
txtNomUP.pack_forget()
lblCorUP.pack_forget()
txtCorUP.pack_forget()
lblConUP.pack_forget()
txtConUP.pack_forget()
btnUP.pack_forget()
btnDlt.pack_forget()


################################################
#creación de las ventanas
panel.add (pestana1, text='Formulario usuarios')
panel.add (pestana2, text='Buscar Usuario')
panel.add (pestana3, text='Consultar usuarios')
panel.add (pestana4, text='Actualizar usuario')


#Funcion para actualizar automaticamente los registros
def Consu(event):
    # verificar si la pestaña seleccionada es la pestaña de Consultar usuarios
    current_tab = event.widget.tab('current')['text']
    if current_tab == 'Consultar usuarios':
        #si es así pues se borran los datos del treeview para evitar que se escriban muchas veces los datos
        for row in tree.get_children():
            tree.delete(row)
        #aqui "a" va a mostrar los registros pero hare uso de un ciclo para mostrar todos los registros.
        a=controlador.Consu()
        while a:
            row = a.pop(0)  
            #aqui se insertan los datos del ciclo en el tree por filas.
            tree.insert('', tk.END, values=(row))   
#investigue esta opcion que ejecuta la función cada que se cambia a la pestaña indicada arriba.
panel.bind('<<NotebookTabChanged>>', Consu)


# función que muestra el botón de actualizar
def Mostrarboton(event):
    #hace uso del if un treeview esta seleccionado, muestra el botón
    if tree.selection():
        # si hay elementos seleccionados, mostrar el botón
        btnUpdate.pack()
    else:
        # si no hay elementos seleccionados, ocultar el botón
        btnUpdate.pack_forget()

# vincular la función al evento <<TreeviewSelect>>
tree.bind('<<TreeviewSelect>>', Mostrarboton)
Ventana.mainloop()
