# Ejercicios mios en el computador



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
