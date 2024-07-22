class PosicionInexistente(Exception):
    pass # el pass indica que no tienen ningún contenido adicional

class NumeroNegativo(Exception):
    pass

class LetraInvalida(Exception):
    pass

lista = [3, 5, 6, 8]

print("Los numeros que hay en la lista", lista, "\n", "Los numeros validos son: 0 1 2 3")

try:
    pos = int(input("ingrese la posición del elemento que desea obtener:"))

    if pos < 0:
        raise NumeroNegativo
    elif pos >= len(lista): # Para asegurar que no se salte el 4
        raise PosicionInexistente
    print(f"El numero en la posicion {pos} es {lista[pos]}")

except ValueError:
    print("Letras no son permitidas")
except NumeroNegativo:
    print("Numeros Negativos no se aceptan")
except PosicionInexistente:
    print("La posición ingresada no existe")


print("\n")

# Ejercicio 2 

lista = [2,5,9,3]
print (lista)
el = int(input("Ingrese elemento: "))

def agregar_una_vez(lista , el):
    try:
        if el in lista:
            raise ValueError(f"Error: No se puede añadir el {el} porque ya esta en la lista")
        lista.append(el)
    except ValueError as e:
        print(e)
    finally:
        print("Gracias por usar este programa :)") 

agregar_una_vez(lista, el)
print("Lista actualizada:", lista)