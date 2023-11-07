class Usuario():

    def __init__(self):
        self.username = []
        self.password = []
        self.reserva = []

    def authenticate(self, input_username:str, input_password:str):
        for i in range(len(self.username)):
            if input_username == self.username[i] and input_password == self.password[i]:
                return True
            
            else:
                return False
