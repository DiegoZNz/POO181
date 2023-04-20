from tkinter import messagebox
import sqlite3

class ControladorBD:
    
    def __init__(self):
        pass
    
    #Metodos para crear conexiones
    def conexionBD(self):
        try:
            conexion= sqlite3.connect("C:/Users/diego/Documents/GitHub/POO181/Examen3erP/BDFerreteria.db")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar a la base de datos")
            
    
    def guardarMaterial(self, nom,cant):
        #1. usamos una conexion 
        conx=self.conexionBD()
        
        #2. validar parámetros vacíos
        if(nom=="" or cant==""):
            messagebox.showwarning("Errorsote","Formulario incompleto")
            conx.close
            return False   
        try:
            #por ultimo validamos que el precio sea un número flotante, si es así se ejecuta la consulta de agregar producto, de lo contrario manda error.
            int(cant)
            #3. Preparamos el cursor, datos que voy a insertar y el querySQL
            cursor= conx.cursor()
            datos=(nom,cant)
            qrInsert="insert into TBMatConstruccion (Material, Cantidad) values (?,?)" 
            #4.Ejecutamos el insert y cerramos la conexion
            cursor.execute(qrInsert,datos)           
            conx.commit()
            conx.close
            messagebox.showinfo("Exito","Material Guardado")
            return True
        except ValueError:
            messagebox.showwarning("Error", "La cantidad debe ser un NÚMERO válido.")
            conx.close
            return False

     
    def ConsultarMateriales(self):
        #1. usamos una conexion 
        conx=self.conexionBD()
        try:
            cursor=conx.cursor()
            selectquery = "SELECT * FROM TBMatConstruccion"
            #4.ejecuta y guarda la consulta
            cursor.execute(selectquery)
            rsProd = cursor.fetchall()
            conx.close()
            #5. retornar resultados en un while
            lista = []
            for row in rsProd:
                lista.append(row)
            return lista

        except sqlite3.OperationalError:
            print("error consulta")
            
    def ActualizarMaterial(self, id,nom,cant):
        #1. usamos una conexion 
        conx=self.conexionBD()
        #2. validar parámetros vacíos
        if(nom=="" or cant==""):
            messagebox.showwarning("Campos incompletos","No puedes actualzar un formulario y dejar campos vacíos")
            return False
        try:
            #por ultimo validamos que el precio sea un número flotante, si es así se ejecuta la consulta de agregar producto, de lo contrario manda error.
            int(cant)
            #3. Preparamos el cursor, datos que voy a insertar y el querySQL
            cursor= conx.cursor()
            datosUP=(nom,cant)
            qrUPD="UPDATE TBMatConstruccion SET Material=?, Cantidad=? Where IDMat="+id
            #4.Ejecutamos el insert y cerramos la conexion
            cursor.execute(qrUPD,datosUP)           
            conx.commit()
            messagebox.showinfo("Exito","Material Actualizado")
            return True
        except ValueError:
            messagebox.showwarning("Error", "La cantidad debe ser un NÚMERO válido.")
            return False
    