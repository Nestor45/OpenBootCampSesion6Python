class Veiculo:
    color = "blanco"
    ruedas = 4
    puertas = 2

class Coche (Veiculo):
    velicidad = 15
    cilindrada = 1.3

c = Coche()
print(c.color)
print(c.ruedas)
print(c.puertas)
print(c.velicidad)
print(c.cilindrada)