def Calcular_Area_Cuadrado():
    Lado = int(input("Ingrese lado del Cuadrado: "))
    Lado2 = int(input("Ingrese lado del Cuadrado: "))
    Area = Lado * Lado2
    print("El area del cuadrado es:" , Area)

def Calcular_Area_Rectangulo():
    Base = int(input("Ingrese la Base del Rectangulo: "))
    Altura = int(input("Ingrese la Altura del Rectangulo: "))
    Area = Base * Altura 
    print("El area del Rectuangulo es:" , Area)

def Calcular_Area_Triangulo():
    Base = int(input("Ingrese la Base del Triangulo: "))
    Altura = int(input("Ingrese la Altura del Triangulo: "))
    Area = (Base * Altura) / 2
    print("El area del Triangulo es:" , Area)

def Calcular_Area_Rombo():
    Diagonal = float(input("Ingrese diagonal del rombo: "))
    Diagonal2 = float(input("Ingrese diagonal del rombo: "))  
    if Diagonal > Diagonal2: 
        diagonal_mayor = Diagonal
        diagonal_menor = Diagonal2
    else:
        diagonal_mayor = Diagonal2
        diagonal_menor = Diagonal
    Area = diagonal_menor * diagonal_mayor
    print("El area del rombo es:", Area) 