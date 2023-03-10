from tkinter import messagebox
import random
import string

class diego:
    def __init__(self, len,mayus,espe):
        self.__longitud=len
        self.__checkmayus=mayus
        self.__checkspe=espe


    def checarSeguridad(self,parametro):
        
        if parametro  < 8:
            messagebox.showerror("contraseña","La contraseña es debil")
        elif parametro  < 12:
            messagebox.showerror("contraseña","La contraseña es buena")
        elif parametro  >= 13:
            messagebox.showerror("contraseña","La contraseña es fuerte")   
                
    def generarContraseña(self,long, include_uppercase=False, include_special=False):
        chars = string.ascii_lowercase
        if include_uppercase:
            chars += string.ascii_uppercase
        if include_special:
            chars += string.punctuation
        password = ''.join(random.choice(chars) for _ in range(long))
        messagebox.showinfo("Contraseña",password)
        return password

