lista1 = input("Ingrese 6 numeros: ") # 0,1,2,3,4,5
lista2 = input("Ingrese 6 numeros: ") 

numeros_lista = lista1.split(',')
numeros = [int(numero) for numero in numeros_lista]
print("Los números ingresados son:", numeros)

numeros_lista2 = lista2.split(',')
numeros2 = [int(numero) for numero in numeros_lista2]
print("Los números ingresados son:", numeros2)

print( "La multiplicacion entre:" , numeros[0] , "y" , numeros2[5] , "es" ,  numeros[0] * numeros2[5])
print( "La multiplicacion entre:" , numeros[1] , "y" , numeros2[4] , "es" , numeros[1] * numeros2[4])
print( "La multiplicacion entre:" , numeros[2] , "y" ,  numeros2[3] , "es" , numeros[2] * numeros2[3])

listac = []
listac.append(numeros[0] * numeros2[5])
listac.append(numeros[1] * numeros2[4])
listac.append(numeros[2] * numeros2[3])

print("Los resultados son:", listac)


