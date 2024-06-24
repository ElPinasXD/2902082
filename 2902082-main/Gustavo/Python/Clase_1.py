print("Ejercicio 1: ") 

cant_Fru = int(input("ingrese cuanta fruta recolecto: ")) 
Cant_F_Pro = int(input("ingrese cuanta fruta producio: "))
indice_C = (cant_Fru / Cant_F_Pro) % 100
print("El indice de cosecha es:" , indice_C )

print("\n")

print("Ejercicio 2: ")

print("+"+ 5 *"-"+"+")
print(("|"+ " "* 5 + "|\n")*3, end="")
print("+"+ 5*"-"+"+")  
print("|\n"*4)


print("\n")

print("Ejercicio 3: ")

nota = float(input("Ingrese nota: "))
nota2 = float(input("Ingrese nota: "))
nota3 = float(input("Ingrese nota: "))
nota4 = float(input("Ingrese nota: "))
nota5 = float(input("Ingrese nota: "))
operacion = (((nota + nota2 + nota3) // 3) * 0.55) + (nota4 *0.30) + (nota5 * 0.15)
print("La calificacion final es: " , operacion)


print("\n")

print("Ejercicio 4: ")

palabra = str(input("Ingrese palabra: "))
print("La palabra" , palabra , "tiene" , len(palabra) , "letras")

print("\n")

print("Ejercicio 5: ")

frase = input("Ingrese la frase: ").upper()
print("Su frase es:", frase[::-1]) 