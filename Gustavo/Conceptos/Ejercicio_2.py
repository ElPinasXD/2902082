
"""

class Persona:
    def __init__(self, nombre, documento, direccion):
        self.__nombre = nombre
        self.__documento = documento
        self.__direccion = direccion
    
    def get_nombre(self):
        return self.__nombre
    
    def get_documento(self):
        return self.__documento
    
    def get_direccion(self):
        return self.__direccion

    def mostrar_informacion(self):
        return f'\nNombre: {self.get_nombre()}\nDocumento: {self.get_documento()}\nDirección: {self.get_direccion()}'
        
class Empleado(Persona):
    def __init__(self, nombre, documento, direccion, codigo_e, empresa, sueldo):
        super().__init__(nombre, documento, direccion)
        self.__codigo_e = codigo_e
        self.__cargo = "Empleado"  
        self.__empresa = empresa
        self.__sueldo = sueldo
    
    def get_codigo_e(self):
        return self.__codigo_e
    
    def get_cargo(self):
        return self.__cargo
    
    def get_empresa(self):
        return self.__empresa
    
    def get_sueldo(self):
        return self.__sueldo
    
    def mostrar_informacion(self):
        info_persona = super().mostrar_informacion()
        info_empleado = f'Código de Empleado: {self.get_codigo_e()}\nCargo: {self.get_cargo()}\nEmpresa: {self.get_empresa()}\nSueldo: {self.get_sueldo()}\n'
        return f'{info_persona}\n{info_empleado}'
        
class Estudiante(Persona):
    def __init__(self, nombre, documento, direccion, codigo_p, programa, trimestre):
        super().__init__(nombre, documento, direccion)
        self.__codigo_p = codigo_p
        self.__programa = programa
        self.__trimestre = trimestre
    
    def get_codigo_p(self):
        return self.__codigo_p
    
    def get_programa(self):
        return self.__programa
    
    def get_trimestre(self):
        return self.__trimestre
    
    def mostrar_informacion(self):
        info_persona = super().mostrar_informacion()
        info_estudiante = f'Código del Programa: {self.get_codigo_p()}\nPrograma: {self.get_programa()}\nTrimestre: {self.get_trimestre()}\n'
        return f'{info_persona}\n{info_estudiante}'

def main():
    while True:
        print("\nSeleccione el tipo de persona para ingresar los datos:")
        print("1. Empleado")
        print("2. Estudiante")
        print("3. Salir")
        
        opcion = input("Ingrese el número de la opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            documento = input("Ingrese el documento: ")
            direccion = input("Ingrese la dirección: ")
            codigo_e = input("Ingrese el código de empleado: ")
            empresa = input("Ingrese la empresa: ")
            sueldo = float(input("Ingrese el sueldo: "))
            empleado = Empleado(nombre, documento, direccion, codigo_e, empresa, sueldo)
            print(empleado.mostrar_informacion())
            
        elif opcion == "2":
            nombre = input("Ingrese el nombre: ")
            documento = input("Ingrese el documento: ")
            direccion = input("Ingrese la dirección: ")
            codigo_p = input("Ingrese el código del programa: ")
            programa = input("Ingrese el programa: ")
            trimestre = input("Ingrese el trimestre: ")
            estudiante = Estudiante(nombre, documento, direccion, codigo_p, programa, trimestre)
            print(estudiante.mostrar_informacion())
            
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()


    Programacion funcional 
        Funciones
    



def Mayuscula(frase):
    return frase.upper()

def Invertir(frase):
    return frase[::-1]

frase = input("Ingrese la frase: ")

mas = (Mayuscula(Invertir(frase)))
print(mas)


# Ejercicio de encriptar la frase y devolver letra diferente
def Encriptar(mensaje, posiciones):
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    resultado = ''
    for letra in mensaje:
            if letra in alfabeto:
                indice = alfabeto.index(letra)
                nuevo_indice = (indice + posiciones) % 27
                resultado += alfabeto[nuevo_indice]
            else:
                resultado += letra
    return resultado  

def Mayuscula(frase):
    return frase.upper()

def Invertir(frase):
    return frase[::-1]

frase = input("Ingrese la frase: ")

mas = Mayuscula(Invertir(Encriptar(frase, 1)))
print(mas)



# Ejercico de que funciones de validar contraseña con cadenas de caracteres 
# y mirar longitud de contraseña para la contraseña


username = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

def Login():
    def validar_usuario():
        
        usuarios = {"user1" : "pass1", "user2" : "pass2" , "user3" : "pass3"}
        if username in usuarios and usuarios[username] == password:
            return True
        else: 
            return False

    if validar_usuario(): 
        print("Inicio de sesion bien")
    else:
        print("Esta mal")
        

Login()



# Funciones dentro de una funcion 
cantidad_numeros = int(input("Ingrese la cantidad de números: "))

numeros = []
for i in range(cantidad_numeros):
    num = int(input(f"Ingrese el número {i+1}: "))  
    numeros.append(num)

def transformar_lista(lista, funcion):
    return [funcion(x) for x in lista]

def siguiente(x):
    return x + 1

def anterior(x):
    return x - 1

def duplicar(x):
    return x * 2

print("Números originales:", numeros)
print("Números sumando 1 :", transformar_lista(numeros, siguiente))
print("Números restando 1:", transformar_lista(numeros, anterior))
print("Números multiplicados:", transformar_lista(numeros, duplicar))

"""

import re

def verificar_contraseña(contraseña):

    caracteres_especiales = "!@#$%^&*(),.?\":{}|<>-"

    if len(contraseña) < 6:
        return False
    if not re.search(r'[A-Z]', contraseña):
        return False
    if not re.search(r'[a-z]', contraseña):
        return False
    if not re.search(r'[0-9]', contraseña):
        return False
    if not any(char in caracteres_especiales for char in contraseña):
        return False
    return True

def registrar_usuarios():
    usuarios = {}

    for i in range(3):
        nombre = input(f"Ingrese el nombre del usuario {i+1}: ").strip()
        while True:
            contraseña = input(f"Ingrese la contraseña: ").strip()
            if verificar_contraseña(contraseña):
                usuarios[nombre] = contraseña
                break
            else:
                print("La contraseña no cumple los requisitos")
    
    print("\nUsuarios registrados")
    for nombre, contraseña in usuarios.items():
        print(f"Usuario: {nombre}  Contraseña: {contraseña}")
    
    return usuarios

def autenticar_usuario(usuarios):
    while True:
        nombre = input("Ingrese el usuario: ").strip()
        contraseña = input("Ingrese contraseña: ").strip()
        
        if nombre in usuarios and usuarios[nombre] == contraseña:
            print("Entro")
            break
        else:
            print("Esta mal")

def main():
    usuarios = registrar_usuarios()
    print("\nPor favor, inicie sesión.")
    autenticar_usuario(usuarios)

if __name__ == "__main__":
    main()

