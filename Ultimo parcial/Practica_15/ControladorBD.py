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
            conx.close()
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
    
    
    def consultarUsuario(self,id):
        
        #1. usamos una conexion 
        conx=self.conexionBD()
        #2. validar parametros Vacios
        
        if(id==""):
            messagebox.showwarning("Aguas","Campo vacío, ponga un id ")
            conx.close()
        else:
            try:
                #3 cursos y query
                cursor=conx.cursor()
                selectquery = "SELECT * FROM TBRegistrados WHERE id="+id
                
                #4.ejecuta y guarda la consulta
                
                cursor.execute(selectquery)
                rsUsuario= cursor.fetchall()
                conx.close()
                return rsUsuario
            except sqlite3.OperationalError:
                print("error consulta")
                
    def Consu(self):
        #1. usamos una conexion 
        conx=self.conexionBD()

        try:
            #3 cursos y query
            cursor=conx.cursor()
            selectquery = "SELECT * FROM TBRegistrados"

            #4.ejecuta y guarda la consulta
            cursor.execute(selectquery)
            rsUsuario = cursor.fetchall()
            conx.close()

            #5. retornar resultados en un while
            results = []
            for row in rsUsuario:
                results.append(row)
            return results

        except sqlite3.OperationalError:
            print("error consulta")
