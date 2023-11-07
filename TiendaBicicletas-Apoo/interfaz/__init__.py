import tkinter as tk
from usuario import *

def ventana_registro():
    root.withdraw()
    ventana_registro = tk.Toplevel(root)
    ventana_registro.title("Registro")
    ventana_registro.geometry("500x500")

    label_registro = tk.Label(ventana_registro, text="Formulario de Registro")
    label_usuario = tk.Label(ventana_registro, text="Ingresa tu usuario")
    entry_usuario = tk.Entry(ventana_registro)
    label_contraseña = tk.Label(ventana_registro, text="Ingresa tu contraseña")
    entry_contraseña = tk.Entry(ventana_registro)
    btn_obtener = tk.Button(ventana_registro, text="Obtener", command=lambda: obtener_registro(entry_usuario,entry_contraseña))

    label_registro.pack()
    label_usuario.pack()
    entry_usuario.pack()
    label_contraseña.pack()
    entry_contraseña.pack()
    btn_obtener.pack()

def obtener_registro(entry_usuario, entry_contraseña):
    user = Usuario()
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    user.username.append(usuario)
    user.password.append(contraseña)

def ventana_ingreso():
    ventana_ingreso = tk.Toplevel(root)
    ventana_ingreso.title("Ingreso")
    ventana_ingreso.geometry("500x500")
    label_ingreso = tk.Label(ventana_ingreso, text="Formulario de Ingreso")
    label_ingreso.pack()

def obtener_ingreso():
    pass

root = tk.Tk()
root.title("Tienda de Bicicletas")
root.geometry("600x600")

label = tk.Label(root, text="Bienvenido a nuestra tienda")
btn_registro = tk.Button(root, text="Registrarse", command=ventana_registro)
btn_ingreso = tk.Button(root, text="Ingresar", command=ventana_ingreso)

label.pack()
btn_registro.pack()
btn_ingreso.pack()


root.mainloop()