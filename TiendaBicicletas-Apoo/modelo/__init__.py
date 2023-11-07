from menu import menu
from registro import *
from tienda_bicicleta import *

def main():
    while True:
        menu()
        opc1 = input("Cual es tu opcion: ")

        if opc1 == "1":
            user = input("Ingrese su usuario: ")
            passw = input("Ingrese su contraseña: ")

            if len(user) >= 6 and len(passw) >= 6:
                Usuario = Registro(user, passw)
            else:
                print("\nEl usuario y La contraseña como minimo deben tener 6 caracteres")

            print("\n")

        if opc1 == "2":
            user = input("Ingrese su usuario: ")
            passw = input("Ingrese su contraseña: ") 
            if Usuario.authenticate(user, passw):
                print("Inicio de sesión exitoso.", "\n")
                tienda_bicicleta(Usuario)
                    
            else:
                print("Credenciales incorrectas.", "\n")
                opc1 = input("Quieres recuperar tus credenciales? (y/n): ")
                if opc1 == "y":
                    Usuario.Recuperar_credenciales()

                if opc1 == "n":
                    pass

        if opc1 == "3":
            break

main()