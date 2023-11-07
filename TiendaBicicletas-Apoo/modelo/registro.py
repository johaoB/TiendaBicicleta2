class Registro:
    username = []
    password = []

    def __init__(self, username:str, password:str):
        self.username.append(username)
        self.password.append(password)
        self.reserva = []

    def authenticate(self, input_username:str, input_password:str):
        for i in range(len(self.username)):
            if input_username == self.username[i] and input_password == self.password[i]:
                return True
            
            else:
                return False
            
    def Recuperar_credenciales(self):
        print("Vuelva a ingresar su usuario y contraseña","\n")
        Usuario = input("Usuario: ")
        Contraseña = input("Contraseña: ")

        for i in range(len(self.username)):
            if Usuario == self.username[i]:
                if Contraseña == self.password[i]:
                    pass
                    
                else:
                    print("Tu contraseña es incorrecta","\n")
                    new_password = input("Ingresa tu nueva contraseña: ")
                    self.password[i] = new_password

            else:
                print("Tu usuario es incorrecto","\n")
                new_username = input("Ingresa tu nuevo usuario: ")
                self.username[i] = new_username
