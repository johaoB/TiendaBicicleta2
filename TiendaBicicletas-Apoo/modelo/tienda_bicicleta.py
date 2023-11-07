from bicicleta import b1,b2,b3,b4
from menu import menu2

def tienda_bicicleta(self):
    print("""Bienvenido usuario
Estas son las bicicletas que ofrecemos por el momento""")
    print("1)", b1, "\n")
    print("2)", b2, "\n")
    print("3)", b3, "\n")
    print("4)", b4, "\n")

    while True:
        menu2()
        opc2 = input("ingrese su opcion: ")
        if opc2 == "1":
            opcion = input("Cual bicicleta quieres reservar?: ")

            if opcion == "1":
                self.reserva.append(b1)
            if opcion == "2":
                self.reserva.append(b2) 
            if opcion == "3":
                self.reserva.append(b3) 
            if opcion == "4":
                self.reserva.append(b4) 
        
        if opc2 == "2":
            self.reserva.clear()
            print("Has pagado tu reserva", "\n")

        if opc2 == "3":
            return
