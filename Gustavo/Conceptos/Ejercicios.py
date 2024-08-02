"""

Encapsulacion = es ocultar la complejidad interna de un objeto y exponer 
solamente una interfaz pública que permita interactuar con él

sobrecarga = hace referencia a la capacidad de tener el mismo método definido más 
de una vez en una clase pero con diferentes cantidades o tipos de parámetros


Sobreescritura = Se refiere a la capacidad de una subclase de modificar o extender 
el comportamiento de un método definido en una superclase

Polimorfismo = Mismo metodo, diferente resultado

Clase abstracta = es una clase que no se pueden instanciar directamente y que definen métodos concretos

from abc import ABC
class MiClaseAbstracta(ABC):


class Operaciones:
   @staticmethod
   def sumar(*args):
    return sum(args)


###############################
print (Operaciones.sumar(3, 4))
print (Operaciones.sumar(4.5, 3.2))
print (Operaciones.sumar(3 ,4, 8, 10, 12))
print (Operaciones.sumar(2.5 ,4, 8.2, 5, 3.5,4,5,6,7,5,3,3,4,5,54,3,34))
print (Operaciones.sumar(3,2,43))



# 1 Ejercicio 
class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo, moneda):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__saldo = saldo
        self.__moneda = moneda

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return True
        return False

    def transferir(self, cantidad, cuenta_destino):
        if self.__moneda == cuenta_destino.moneda and 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            cuenta_destino.depositar(cantidad)
            return True
        return False

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def moneda(self):
        return self.__moneda

# Ejemplo de uso
cuenta1 = CuentaBancaria("123", "Juan Perez", 1000, "USD")
cuenta2 = CuentaBancaria("456", "Maria Lopez", 2000, "USD")
cuenta3 = CuentaBancaria("789", "Pedro Gomez", 1500, "EUR")


print(cuenta1.saldo)  # 1000
cuenta1.depositar(500)
print(cuenta1.saldo)  # 1500
cuenta1.retirar(200)
print(cuenta1.saldo)  # 1300
cuenta1.transferir(300, cuenta2)
print(cuenta1.saldo)  # 1000
print(cuenta2.saldo)  # 2300


# Intentar transferir entre cuentas de diferentes monedas
resultado_transferencia = cuenta1.transferir(100, cuenta3)
print(f"Transferencia exitosa: {resultado_transferencia}")  # False
print(cuenta1.saldo)  # 1000
print(cuenta3.saldo)  # 1500




# 2 Ejercicio

from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

def main():
    while True:
        print("Seleccione el tipo de figura para calcular el área:")
        print("1. Círculo")
        print("2. Cuadrado")
        print("3. Triángulo")
        print("4. Salir")
        
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            figura = Circulo(radio)
            print(f'Área del Círculo: {figura.calcular_area()}')
        elif opcion == "2":
            lado = float(input("Ingrese el lado del cuadrado: "))
            figura = Cuadrado(lado)
            print(f'Área del Cuadrado: {figura.calcular_area()}')
        elif opcion == "3":
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            figura = Triangulo(base, altura)
            print(f'Área del Triángulo: {figura.calcular_area()}')
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()


#Ejercicio 3

from abc import ABC, abstractmethod

class Juego(ABC):
    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def mostrar_puntaje(self):
        pass

    @abstractmethod
    def terminar(self):
        pass

class JuegoSimple(Juego):
    def __init__(self):
        self.puntaje = 0

    def iniciar(self):
        print("Juego iniciado")
        input("Presione cualquier tecla para continuar...")
        self.puntaje = 0

    def mostrar_puntaje(self):
        print(f"Puntaje actual: {self.puntaje}")

    def terminar(self):
        print("Juego terminado")
        self.mostrar_puntaje()

    def ganar_puntos(self, puntos):
        self.puntaje += puntos

def menu():
    juego = JuegoSimple()
    juego.iniciar()
    
    while True:
        print("\nSeleccione una opción:")
        print("1. Mostrar puntaje")
        print("2. Ganar puntos")
        print("3. Terminar")
        
        opcion = input("Ingrese el número de la opción: ")
        
        if opcion == "1":
            juego.mostrar_puntaje()
        elif opcion == "2":
            puntos = int(input("Ingrese la cantidad de puntos a ganar: "))
            juego.ganar_puntos(puntos)
        elif opcion == "3":
            juego.terminar()
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()

"""