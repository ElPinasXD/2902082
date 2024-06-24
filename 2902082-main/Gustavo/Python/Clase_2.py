# Ejercicio 1

edad = int(input("Ingrese su edad: "))
if edad >= 18 and edad <= 25:
    print("Es joven")
else:
    print("Fuera de rango") 
   


# Ejercicio 2

edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 5:
    print("Bebe")
elif edad >= 6 and edad <= 12:
    print("Niño")
elif edad >= 13 and edad <= 18:
    print("Adolecente")
elif edad >= 19 and edad <= 45:
    print("Adulto")
elif edad >= 46 and edad <= 90:
    print("Mayor")
elif edad >= 96:
    print("Se nos va a ir a un mundo mejor")



# Ejercicio 3

Tiempo = int(input("Cuanto años lleva en la empresa: "))
Salario = int(input("Cuanto gana: "))

if Tiempo < 1:
    print("Su salario es: " ,  Salario * 0.05)
else:
    if Tiempo >= 1 and Tiempo < 2:
        print("Su salario es:" , Salario * 0.07)
    elif Tiempo >= 2 and Tiempo <= 5:
        print("Su salario es:" , Salario * 0.1)
    elif Tiempo >= 5 and Tiempo <= 10:
        print("Su salario es:" , Salario * 0.15)
    elif Tiempo >= 10:
        print("Su salario es:" , Salario * 0.20)

# Ejercicio 4

numeros = [int(input("Ingrese número {}: ".format(i))) for i in range(1, 4)]
print(sorted(numeros))


Edad = int(input("Cuantos años tiene: "))
Estrato = int(input("Cual es tu estrato: "))
Matricula = int(input("A cuanto esta tu matricula: "))
if Estrato == 1 and Edad < 18:
    print("Su matricula le queda en: " , Matricula * 0.2 )
elif Estrato == 1 and Edad >= 18:
    print("Su matricula le queda en: " , Matricula * 0.15 )
elif Estrato == 2 and Edad < 18:
    print("Su matricula le queda en: " , Matricula * 0.01 )
elif Estrato == 2 and Edad >= 18:
    print("Su matricula le queda en: " , Matricula * 0.5 )
    
# Ciclo WHILE

x = 5
while x <= 50:
    print("5 x", x//5, "=", x)
    x +=5

# Para terminar, ejercicio 7

numero = int(input("Ingrese el último dígito de la placa del automóvil: "))

color = ""

while color == "":
    if  numero == 1 or  numero  == 2:
        color = "Amarillo"
    elif  numero  == 3 or  numero  == 4:
        color = "Rosa"
    elif  numero  == 5 or  numero  == 6:
        color = "Roja"
    elif  numero  == 7 or  numero  == 8:
        color = "Verde"
    elif  numero  == 9 or  numero  == 0:
        color = "Azul"
print("El color de la calcomanía es:", color)

for x in range (1, 11):
     print("1 x", x, "=", 1 * x)


for Tabla in range (1, 11):  # for es un bucle - nombre de variable - range - (parametros)
    for x in range (1, 11):
        c=Tabla*x
        print(Tabla , "x" , x, "=" , c)
    print("=====================\n")



x = 1
while x <= 10:
    print("1 x", x, "=", 1 * x)
    x += 1

x = 1
while x <= 10:
    print("10 x", x, "=", 10 * x)
    x += 1
