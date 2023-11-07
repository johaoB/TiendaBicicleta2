class Bicicleta:
    def __init__(self, marca:str, modelo:int, precio:float):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"""Marca: {self.marca}
Modelo: {self.modelo}
Precio: {self.precio}"""


b1 = Bicicleta("BMC",2020,370.0)
b2 = Bicicleta("MTB",1995,110.0)
b3 = Bicicleta("Banshee",2014,225.0)
b4 = Bicicleta("Diamondback",2009, 270.0)
