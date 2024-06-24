# 1 

Dinero = float(input("Cuánto dinero va a ingresar: "))
Tasa_Interes = float(input("A cuánto la tasa de interés anual: ")) / 100
Años = int(input("Por cuántos años hará la inversión: "))

Inversion = round(Dinero * (1 + Tasa_Interes) ** Años, 2) # Para redondiar en 2 numeros después de la coma 
print("La inversion inicial es de:" , Inversion)

Interes = Inversion - Dinero
if Interes >= 7000 / 100:
    Inversion += Interes
    print("Después de reinvertir los intereses, el total de dinero en su cuenta es:", round(Inversion, 2))
else:
    print("Gracias por su inversión")


# 2 

numeros = [float(input("Ingrese nota: ".format(i))) for i in range(1, 4)] # i = el rango que le limita (1,3)
Promedio = sum(numeros) // 3

if Promedio >= 7.0:
    print("El alumno ha aprobado el curso con un promedio de:", Promedio)
else:
    print("El alumno ha reprobado el curso con un promedio de:", Promedio)


# 3

Horas = int(input("Ingrese cuantas horas trabajo:"))
Hora_Extra = input("¿Ha echo horas extra?:").lower()  # Convertir la entrada a minúsculas para evitar sensibilidad a mayúsculas
if Hora_Extra == "si":
    Cuantas = int(input("¿Cuántas horas extra hizo?: "))
    if Horas <= 40:
        salario = print("Su salario es:" , Horas * 40000 + Cuantas * 30000)
    else:
        salario = print("Su salario es:" ,  40 * 60000 + (Horas - 40) * 30000 + Cuantas * 30000)
elif Hora_Extra == "no":
    if Horas <= 40:
        salario = print("Su salario es:" , Horas * 40000)
    else:
        salario = print("Su salario es:" , 40 * 60000)
else:
    print("Respuesta no válida. Por favor ingrese 'si' o 'no'.")


# 4
numeros = [int(input("Ingrese número {}: ".format(i))) for i in range(1, 4)]
print(sorted(numeros))


# 5

Llantas = int(input("Cuantas llantas va a comprar: "))

if Llantas < 5:
    print("Le quedaria en:" , 800 * Llantas)
else:
    print("Le quedaria en:" ,  700 * Llantas)

# 6 

Puntos = [int(input("Ingrese los puntos IMECA del día {}: ".format(dia))) for dia in range(1, 6)]

Promedio = sum(Puntos) // 5
print(Promedio)

if Promedio > 170:
    print("Detenida la producción por una semana y multa del 50% de las ganancias diarias")
    ganancias_diarias = int(input("Ingrese las ganancias diarias de la fábrica: "))
    multa = 0.5 * ganancias_diarias * 7 
    print("La multa a pagar es:", multa)
else:
    print("Sigan")


# 7

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


# 8

import random

Producto = str(input("Cual es su producto:"))
Precio = int(input("A cuanto esta:"))

Ball_White = Precio
Ball_Green = 0.10 * Precio
Ball_Yellow = 0.25 * Precio
Ball_Blue = 0.50 * Precio
Ball_Red = "Gratis"

opciones = [("Blanca", Ball_White), ("Verde", Ball_Green), ("Amarilla", Ball_Yellow), ("Azul", Ball_Blue), ("Roja", Ball_Red)]

i = random.choice(opciones)
nombre_pelota, valor_pelota = i

print("La pelota que salio fue:", nombre_pelota)

print("Su" , Producto , "le queda en" , valor_pelota)

# 9

edad_persona = int(input("Ingrese la edad de la persona: "))
antiguedad_empleo_persona = int(input("Ingrese la antigüedad en años de la persona en su empleo: "))

def clasificar_jubilacion(edad, antiguedad_empleo):
    if edad >= 60 and antiguedad_empleo < 25:
        return "Jubilación por Edad"
    elif edad < 60 and antiguedad_empleo >= 25:
        return "Jubilación por Antigüedad Joven"
    elif edad >= 60 and antiguedad_empleo >= 25:
        return "Jubilación por Antigüedad Adulta"
    else:
        return "No cumple requisitos de jubilación"

tipo_jubilacion = clasificar_jubilacion(edad_persona, antiguedad_empleo_persona)
print("La persona queda adscrita a la jubilación:", tipo_jubilacion)

# 10

def verificar_anemia(edad, sexo, nivel_hemoglobina):
    if edad <= 0:  # Menos de un año
        if nivel_hemoglobina < 13 or nivel_hemoglobina > 26:
            return "Positivo"
    elif edad <= 1:  # 1 año o más
        if nivel_hemoglobina < 12 or nivel_hemoglobina > 16:
            return "Positivo"
    elif edad <= 5:  # > 1 y <= 5 años
        if nivel_hemoglobina < 11.5 or nivel_hemoglobina > 15:
            return "Positivo"
    elif edad <= 10:  # > 5 y <= 10 años
        if nivel_hemoglobina < 12.6 or nivel_hemoglobina > 15.5:
            return "Positivo"
    elif edad <= 15:  # > 10 y <= 15 años
        if nivel_hemoglobina < 13 or nivel_hemoglobina > 15.5:
            return "Positivo"
    elif sexo == "mujer" and edad > 15:  # mujeres > 15 años
        if nivel_hemoglobina < 12 or nivel_hemoglobina > 16:
            return "Positivo"
    elif sexo == "hombre" and edad > 15:  # hombres > 15 años
        if nivel_hemoglobina < 14 or nivel_hemoglobina > 18:
            return "Positivo"
    
    return "Negativo"

edad_input = input("Ingrese la edad de la persona (si es mes, porfavor _ mes): ")
if "mes" in edad_input:
    edad = int(edad_input.split()[0]) / 12  # Convertir meses a años
else:
    edad = int(edad_input)

sexo = input("Ingrese el sexo de la persona (mujer/hombre): ").lower()
nivel_hemoglobina = float(input("Ingrese el nivel de hemoglobina de la persona (en g%): "))

resultado = verificar_anemia(edad, sexo, nivel_hemoglobina)
print("El resultado es:", resultado)


# CICLOS 

1


ingresar= int(input("¿cuantos nums quiere ingresar?"))
positivos=[]
negativos=[]
for leer in range(ingresar):
    numeros = int(input("Ingresa el numero", leer + 1))
    if numeros > 0:
      positivos.append(numeros)
    elif numeros < 0:
      negativos.append(numeros)

if positivos:
    promedio_p= sum(positivos) / len(positivos)
else:
    promedio_p= 0
    print("No se ingresaron números positivos")


if negativos:
    promedio_n= sum(negativos) / len(negativos)
else:
    promedio_n= 0
    print("No se ingresaron números negativos")

print(" el promedio de los positivos es:", promedio_p)
print(" el promedio de los negativos es:", promedio_n)


2


n = int(input("¿Cuántos elementos deseas en la serie? "))

serie = [1]
for i in range(1, n):
    nuevo_elemento = sum(serie)
    serie.append(nuevo_elemento)

print("Serie generada:")
print(serie)

suma_impares = sum(x for x in serie if x % 2 != 0)

numero_a_verificar = int(input("Introduce un número para verificar si pertenece a la serie: "))
pertenece_a_serie = numero_a_verificar in serie

suma_total = sum(serie)

print(f"La suma de los números impares en la serie es: {suma_impares}")
print(f"El número {numero_a_verificar} {'sí' if pertenece_a_serie else 'no'} pertenece a la serie.")
print(f"La suma de todos los valores de la serie es: {suma_total}")


3

calificaciones = []
for calculo in range(40):
    calificacion = float(input(f"Ingrese la calificación del alumno", calculo + 1 ))
    calificaciones.append(calificacion)

calificacion_media = sum(calificaciones) / 40
calificacion_mas_baja = min(calificaciones)

print(f"La calificación media del grupo es:" ,calificacion_media)
print(f"La calificación más baja del grupo es:" , calificacion_mas_baja)


4

numero = int(input("Introduce un número a multiplicar: "))

print("Tabla de multiplicar del" ,numero ,":")
for multiplicador in range(1, 11):
    producto = numero * multiplicador
    print(numero, "x",multiplicador, "=" , producto)


5


n = int(input("Introduce el número de personas: "))

total_pn = total_n = total_pj = total_j = total_pa = total_a = total_pv = total_v = 0

for i in range(n):
    e = int(input(f"Edad de la persona {i + 1}: "))
    p = float(input(f"Peso de la persona {i + 1} (kg): "))
    if 0 <= e <= 12: total_pn += p; total_n += 1
    elif 13 <= e <= 29: total_pj += p; total_j += 1
    elif 30 <= e <= 59: total_pa += p; total_a += 1
    elif e >= 60: total_pv += p; total_v += 1

ppn = total_pn / total_n if total_n else 0
ppj = total_pj / total_j if total_j else 0
ppa = total_pa / total_a if total_a else 0
ppv = total_pv / total_v if total_v else 0

print("\nResultados del muestreo:")
print(f"Promedio de peso de los niños: {ppn:.2f} kg")
print(f"Promedio de peso de los jóvenes: {ppj:.2f} kg")
print(f"Promedio de peso de los adultos: {ppa:.2f} kg")
print(f"Promedio de peso de los viejos: {ppv:.2f} kg")


6 

amarilla = rosa = roja = verde = azul = 0

n = int(input("Introduce el número de autos: "))

for _ in range(n):
    digito = int(input("Introduce el último dígito de la placa: "))
    if digito == 1 or digito == 2:
        amarilla += 1
    elif digito == 3 or digito == 4:
        rosa += 1
    elif digito == 5 or digito == 6:
        roja += 1
    elif digito == 7 or digito == 8:
        verde += 1
    elif digito == 9 or digito == 0:
        azul += 1

print("Cantidad de autos con calcomanía amarilla:", amarilla)
print("Cantidad de autos con calcomanía rosa:", rosa)
print("Cantidad de autos con calcomanía roja:", roja)
print("Cantidad de autos con calcomanía verde:", verde)
print("Cantidad de autos con calcomanía azul:", azul)


7

n = int(input("Introduce el número de alumnos: "))

total = 0

for _ in range(n):
    calificacion = float(input("Introduce la calificación del alumno: "))
    total += calificacion

promedio = total / n

print("El promedio de calificaciones es:", promedio)


8


n = int(input("Introduce el número de alumnos: "))

total_hombres = total_mujeres = total_edades = 0

for _ in range(n):
    edad = int(input("Introduce la edad del alumno: "))
    genero = input("Introduce el género del alumno (H/M): ").upper()
    
    if genero == "H":
        total_hombres += 1
    else:
        total_mujeres += 1
        
    total_edades += edad

promedio_hombres = total_edades / total_hombres if total_hombres > 0 else 0
promedio_mujeres = total_edades / total_mujeres if total_mujeres > 0 else 0
promedio_total = total_edades / n

print("El promedio de edades de hombres es:", promedio_hombres)
print("El promedio de edades de mujeres es:", promedio_mujeres)
print("El promedio de edades del grupo es:", promedio_total)


9 

n = int(input("Introduce la cantidad de números: "))

maximo = float('-inf')

for _ in range(n):
    numero = float(input("Introduce un número: "))
    if numero > maximo:
        maximo = numero

print("El mayor valor es:", maximo)


10


def calcular_descuento(edad):
    if edad < 5:
        return 0
    elif 5 <= edad <= 14:
        return 0.35
    elif 15 <= edad <= 19:
        return 0.25
    elif 20 <= edad <= 45:
        return 0.10
    elif 46 <= edad <= 65:
        return 0.25
    else:
        return 0.35

n = int(input("Introduce el número de clientes: "))
precio_asiento = float(input("Introduce el precio del asiento: "))

total_descuento = 0

for _ in range(n):
    edad_cliente = int(input("Introduce la edad del cliente: "))
    descuento = calcular_descuento(edad_cliente) * precio_asiento
    total_descuento += descuento

print("El total de dinero que el teatro deja de percibir por descuentos es:", total_descuento)


11


n = int(input("Introduce el número de tarjetas de censo: "))
contador = 0

for _ in range(n):
    numero_censo = int(input("Número de censo: "))
    sexo = input("Sexo (M/F): ")
    edad = int(input("Edad: "))
    estado_civil = input("Estado civil (S/C/V/D): ").upper()
    
    if sexo == "F" and estado_civil == "S" and 16 <= edad <= 21:
        contador += 1

print("Número de jóvenes solteras entre 16 y 21 años:", contador)


12

altura_inicial = 100
altura_actual = altura_inicial
tiempo = 0

while altura_actual > 0:
    tiempo += 1
    altura_actual = altura_inicial - 0.5 * 9.8 * tiempo ** 2
    if altura_actual > 0:
        print(f"En el segundo {tiempo / 10:.1f}, la altura es {altura_actual:.2f} metros.")

print(f"El objeto toca el suelo en {tiempo / 10:.1f} segundos.")


13

n = 100
calificaciones = []

for _ in range(n):
    calificacion = float(input("Introduce la calificación del estudiante: "))
    calificaciones.append(calificacion)

menor_a_50 = sum(1 for calificacion in calificaciones if calificacion < 50)
entre_50_y_80 = sum(1 for calificacion in calificaciones if 50 <= calificacion < 80)
entre_70_y_80 = sum(1 for calificacion in calificaciones if 70 <= calificacion < 80)
mayor_o_igual_80 = sum(1 for calificacion in calificaciones if calificacion >= 80)

print("Cantidad de estudiantes con calificación menor a 50:", menor_a_50)
print("Cantidad de estudiantes con calificación entre 50 y 80:", entre_50_y_80)
print("Cantidad de estudiantes con calificación entre 70 y 80:", entre_70_y_80)
print("Cantidad de estudiantes con calificación mayor o igual a 80:", mayor_o_igual_80)


14


def fibonacci(n):
    a, b = 0, 1
    suma = 0
    while b < n:
        if b % 2 == 0:
            suma += b
        a, b = b, a + b
    return suma

resultado = fibonacci(10000)
print("La suma de los términos de la serie Fibonacci entre 100 y 10,000 es:", resultado)



15 

from datetime import datetime

fecha_nacimiento = input("Introduce tu fecha de nacimiento (formato: AAAA-MM-DD): ")
fecha_actual = datetime.now()

nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
diferencia = fecha_actual - nacimiento
dias_vividos = diferencia.days

print("Número de días vividos hasta la fecha:", dias_vividos)
