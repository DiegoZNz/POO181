import tkinter as tk
from tkinter import ttk, font
from tkinter import *
from Logica import *

controlador=ControladorBD()

def nuevo():
    panel.add (pestana2, text='Agregar')
    txtNom.delete("0", "end")
    txtCant.delete("0", "end")
    panel.select(1)
    btna.pack()
    btnactu.pack_forget()

def agregar():
    if controlador.guardarMaterial(varNom.get(),varCant.get()):
        txtNom.delete("0", "end")
        txtCant.delete("0", "end")
        panel.forget(1)
        panel.select(0)

def modificar():
    panel.add (pestana2, text='Modificar')
    btnactu.pack()
    btna.pack_forget()
    txtNom.delete("0", "end")
    txtCant.delete("0", "end")
    selected = tree.selection()[0]
    # obtener los valores del elemento seleccionado
    values = tree.item(selected)['values']
    txtId.insert(0, values[0])
    txtNom.insert(0, values[1])
    txtCant.insert(0, values[2])
    panel.select(1)





Ventana= Tk()
Ventana.title("Ferreteria")
Ventana.geometry("700x400")

panel=ttk.Notebook (Ventana)
panel.pack(fill='both', expand='yes')
pestana1=ttk.Frame (panel)
pestana2=ttk.Frame (panel)


panel.add (pestana1, text='Consultar')

fuente = font.Font(family='Helvetica', size=12, weight='bold')
TituloCons=Label(pestana1,text="Consultar Material", fg="blue").pack()


columns = ('ID', 'Material', 'Cantidad')
tree = ttk.Treeview(pestana1, columns=columns, show='headings')
tree.heading("ID", text="ID")
tree.heading("Material", text="Material")
tree.heading("Cantidad", text="Cantidad")
tree.pack()
btnUpdate=Button(pestana1, text='Actualizar',command=modificar)
#pero se oculta para que se ejecute solamente cuando se presiona un registro(para evitar bugs y errores por los usuarios)
btnUpdate.pack_forget()

BtnAdd = Button(pestana1,text='Nuevo Material',command=nuevo).pack()

#pestaña 2 
titulo = Label(pestana2, text="Agregar Materiales", fg="blue", font=fuente)
titulo.pack()

varIdUp=tk.StringVar()
txtId= Entry(pestana2, textvariable=varIdUp)

varNom = tk.StringVar()
lblNom = Label(pestana2, text="Nombre del material: ")
lblNom.pack()
txtNom = Entry(pestana2, textvariable=varNom)
txtNom.pack()

varCant = tk.StringVar()
lblCant = tk.Label(pestana2, text="Cantidad: ")
lblCant.pack()
txtCant = tk.Entry(pestana2, textvariable=varCant)
txtCant.pack()
btna=Button(pestana2,text="Agregar",command=agregar)

btnactu=Button(pestana2,text="Actualizar")



def Consultar(event):
    # verificar si la pestaña seleccionada es la pestaña de Consultar usuarios
    current_tab = event.widget.tab('current')['text']
    if current_tab == 'Consultar':
        #si es así pues se borran los datos del treeview para evitar que se escriban muchas veces los datos
        for row in tree.get_children():
            tree.delete(row)
        #aqui "a" va a mostrar los registros pero hare uso de un ciclo para mostrar todos los registros.
        a=controlador.ConsultarMateriales()
        while a:
            row = a.pop(0)  
            #aqui se insertan los datos del ciclo en el tree por filas.
            tree.insert('', tk.END, values=(row))   
#investigue esta opcion que ejecuta la función cada que se cambia a la pestaña indicada arriba.
panel.bind('<<NotebookTabChanged>>', Consultar)


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