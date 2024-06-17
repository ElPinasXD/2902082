#1 ejercicio

lista = (2,3,56,4,8)
print("El numero mas grande entre" , lista , "es:" , max(lista))

# 2 ejercicio

numeros = [1,2,3,5,7,8]
print("La suma de" , numeros , "es", sum(numeros))


# 3 ejercicio

repetir = [1,1,1,2,3,4,5,5]
elemento = 1  # El elemento que quieres contar
veces_repetido = repetir.count(elemento)
print("El elemento", elemento, "aparece", veces_repetido, "veces en la lista.")

# Con interacion al usuario

repetir = [int(input("Ingrese número {}: ".format(i))) for i in range(1, 11)]
cual = int(input("Cual numero deseas saber, cuantas veces se repite"))
veces_repetido = repetir.count(cual)
print("El elemento", cual, "aparece", veces_repetido, "veces en la lista.")


# Para que me diga cada uno

repetir = [1,1,1,2,3,4,5,5]
# Creamos un diccionario para almacenar los recuentos de cada elemento
recuentos = {}
for elemento in repetir:
    if elemento in recuentos:
        recuentos[elemento] += 1
    else:
        recuentos[elemento] = 1

# Imprimimos los recuentos
for elemento, contador in recuentos.items():
    print("El elemento", elemento, "aparece", contador, "veces en la lista.")



# 4 ejercicio 

numeros = [1,2,3,4,5,6,7,8]
numeros.sort(reverse=True)
print(numeros) 

# 5 ejercicio - Para que borre los elementos duplicados

numeros = [1,1,1,1,1,2,3,4,5,6,7,8]
numeros_bloqueados = list(set(numeros))
print(numeros_bloqueados)

# 6 ejercicio - para juantar los elementos

numeros_1 = [1,2,3,4,5,6,7,8]
numeros_2 = [3,6,8,2,1,5,5]

for x in zip (numeros_1, numeros_2):
    print(x)

# 7 ejercicio - Para que me cuente cuantas veces aparece cierta letra

oracion = str(input("Ingrese una frase: "))
recuentos = {}
for elemento in oracion:
    if elemento in recuentos:
        recuentos[elemento] += 1
    else:
        recuentos[elemento] = 1
for elemento, contador in recuentos.items():
    print("La letra", elemento, "aparece", contador, "veces en la oracion")


# 8 ejercicio - hace una multiplicacion por el mismo numero 1*1 hasta que el usuario diga que numero 

Numero = int(input("Ingrese un numero: "))
cuadrado = {}
for x in range(1,Numero+1):
    cuadrado[x] = x ** 2
for x, Resultado in cuadrado.items():
    print( x, "->" , Resultado)



# 9 ejercicio - Falta

def main():
  """
  Programa principal que implementa la venta de frutas.
  """

  # Diccionario para almacenar los precios de las frutas
  precios_frutas = {
    "manzana": 1.5,
    "pera": 2.0,
    "platano": 1.0,
    "naranja": 0.8,
  }

  # Bucle infinito para realizar múltiples ventas
  while True:
    # Solicitar el nombre de la fruta
    nombre_fruta = input("Ingrese el nombre de la fruta: ").lower()

    # Verificar si la fruta existe en el diccionario
    if nombre_fruta in precios_frutas:
      # Solicitar la cantidad vendida
      cantidad = float(input("Ingrese la cantidad vendida: "))

      # Calcular el precio total
      precio_total = precios_frutas[nombre_fruta] * cantidad

      # Mostrar el precio total
      print(f"El precio total de la {nombre_fruta} es: {precio_total:.2f}")

    else:
      # Mostrar mensaje de error si la fruta no existe
      print(f"La fruta '{nombre_fruta}' no existe en el inventario.")

    # Preguntar si se desea realizar otra venta
    otra_venta = input("¿Desea realizar otra venta? (s/n): ").lower()

    if otra_venta != "s":
      break

if __name__ == "__main__":
  main()
