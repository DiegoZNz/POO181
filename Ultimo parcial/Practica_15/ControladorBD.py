from tkinter import messagebox
import sqlite3
import bcrypt

class ControladorBD:
    
    def __init__(self):
        pass
    
    
    #Metodos para crear coexiones
    def conexionBD(self):
        try:
            conexion= sqlite3.connect("C:/Users/diego/Documents/GitHub/POO181/Ultimo parcial/Practica_15/tkinterSQLite/DBUsuarios.db")
            print("conectado a la base de datos")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar a la base de datos")
            
    #Metodo para guardar usuarios
    def guardarUsuario(self, nom,cor,con):
        #1. usamos una conexion 
        conx=self.conexionBD()
        
        #2. validar parametros Vacios
        
        if(nom=="" or cor=="" or con==""):
            messagebox.showwarning("Aguas","Formulario incompleto")
        else:
            #3. Preparamos el cursor, datos que voy a insertar y el querySQL
            
            cursor= conx.cursor()
            
            conH=self.encriptarCon(con)
            
            datos=(nom,cor,conH)
            qrInsert="insert into TBRegistrados (Nombre, Correo, Contra) values (?,?,?)" 
            
            #4.Ejecutamos el insert y cerramos la conexion
            cursor.execute(qrInsert,datos)           
            conx.commit()
            conx.close
            messagebox.showinfo("Exito","Usuario Guardado")
            
    def encriptarCon(self, contra):
        ConPlana= contra
        
        ConPlana = ConPlana.encode() # convertimos a bytes
        
        sal= bcrypt.gensalt()
        conHa = bcrypt.hashpw(ConPlana,sal)
        print (conHa)
        return conHa