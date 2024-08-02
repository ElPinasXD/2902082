"""

Herencia:

class Subclase (Superclase):
        !           !
class Empleado   (Persona)

Herencia multiple 

class    Subclase       (Superclase1, Superclase2, Superclase_n):
            !                !               !           !
class EstudianteMusico  (Estudiante,      Persona,    Musico):


super() = permite acceder a los miembros de la superclase

issubclass() = es una función que nos permite comprobar si una clase es subclase de otra
print (issubclass(Empleado, Persona)) # True 
print (issubclass(Persona, Empleado))

Asosiacion = Se conocen la estructura y los parametros 
Agregacion = es una relación entre dos clases en la que una clase contiene una o varias
instancias de otra clase como parte de su estructura
Composicion = es una relación entre dos clases en la que una clase contiene a otra clase 
como parte de su estructura y es responsable de crear y destruir las instancias de la clase contenida


class Persona:

  def __init__(self, nombre, edad):  #constructor de la superclase
    self.__nombre = nombre
    self.__edad = edad

  def cumplir_anos(self):
    self.__edad += 1

  def devolver_nombre(self):
    return self.__nombre

  def devolver_edad(self):
    return self.__edad

class Empleado(Persona):
  def __init__(self, nombre, edad, salario): #constructor de la subclase
    super().__init__(nombre, edad)  #envía el nombre y edad al constructor de la superclase
    self.__salario = salario

  def devolver_salario(self):
    return self.__salario

###########################################
emp = Empleado ("Juan", 30, 1_500_000)  #se crea un empleado (sublcase)
emp.cumplir_anos()
print (f"nombre del empleado: {emp.devolver_nombre()}")
print (f"edad del empleado: {emp.devolver_edad()}")
print (f"salario del empleado: {emp.devolver_salario()}")


class Vehiculo:
    def __init__(self, modelo):
        self.modelo = modelo

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculo = None

    def comprar_vehiculo(self, vehiculo:Vehiculo):
        self.vehiculo = vehiculo

    def conducir_vehiculo(self):
        if self.vehiculo is not None:
            print(f"{self.nombre} está conduciendo un vehículo {self.vehiculo.modelo}")
        else:
            print(f"{self.nombre} no tiene un vehículo para conducir")
#########################################################################

persona1 = Persona("Juan")
vehiculo1 = Vehiculo("Toyota")
persona1.comprar_vehiculo(vehiculo1)
persona1.conducir_vehiculo()

persona2 = Persona("Pedro")
persona2.conducir_vehiculo()


class Celular:
    def __init__(self, numero):
        self.numero = numero
    #def __str__(self):
    #  return self.numero

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.celulares = []

    def agregar_celular(self, celular:Celular):
        self.celulares.append(celular)

    def mostrar_celulares(self):
        print ("celulares de ", self)
        for cel in self.celulares:
          print (cel.numero)

    def quitar_celular(self, num):
      for c in self.celulares:
        if c.numero == num:
          self.celulares.remove(c)

    def __str__(self):
      return self.nombre
#####################################################
p = Persona ("Juan")
c1 = Celular (300248)
c2 = Celular (320789)
c3 = Celular (311445)

p.agregar_celular(c1)
p.agregar_celular(c2)
p.agregar_celular(c3)

p.mostrar_celulares()

p.quitar_celular(320789)
p.mostrar_celulares()

print("numero del cel 2: ", c2.numero)



# Primer ejercicio 

class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre

    def __str__(self):
        return f'Cliente: {self.nombre}, Cédula: {self.cedula}'

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def obtener_numero_clientes(self):
        return len(self.clientes)

    def obtener_clientes(self):
        return [str(cliente) for cliente in self.clientes]

    def __str__(self):
        return f'Banco: {self.nombre}, Número de clientes: {self.obtener_numero_clientes()}'

# Ejemplo de uso
cliente1 = Cliente("12345", "Juan Perez")
cliente2 = Cliente("67890", "Maria Lopez")

banco = Banco("Banco Central")
banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)

print(banco)
print(banco.obtener_clientes())



# Segundo Ejercico

class Cuenta:
    def __init__(self, numero, tipo, saldo):
        self.numero = numero
        self.tipo = tipo
        self.saldo = saldo

    def __str__(self):
        return f'Cuenta: {self.numero}, Tipo: {self.tipo}, Saldo: {self.saldo}'

class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def __str__(self):
        cuentas_info = "\n".join(str(cuenta) for cuenta in self.cuentas)
        return f'Cliente: {self.nombre}, Cédula: {self.cedula}\nCuentas\n{cuentas_info}'

class Banco:
    __instance = None
    __initialized = False

    def __new__(cls, nombre=None):
        if cls.__instance is None:
            cls.__instance = super(Banco, cls).__new__(cls)
        return cls.__instance

    def __init__(self, nombre):
        if not self.__initialized:
            self.nombre = nombre
            self.clientes = []
            Banco.__initialized = True

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def obtener_numero_clientes(self):
        return len(self.clientes)

    def obtener_clientes(self):
        return [str(cliente) for cliente in self.clientes]

    def ver_info_clientes(self):
        return "\n".join(self.obtener_clientes())

    def total_saldos_ahorros(self):
        total = 0
        for cliente in self.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.tipo == "ahorros":
                    total += cuenta.saldo
        return total

    def total_saldos_corriente(self):
        total = 0
        for cliente in self.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.tipo == "corriente":
                    total += cuenta.saldo
        return total

    def __str__(self):
        return f'Banco: {self.nombre}, Número de clientes: {self.obtener_numero_clientes()}'

# Ejemplo de uso
cliente1 = Cliente("12345", "Juan Perez")
cuenta1 = Cuenta("0001", "ahorros", 1000)
cuenta2 = Cuenta("0002", "corriente", 2000)
cliente1.agregar_cuenta(cuenta1)
cliente1.agregar_cuenta(cuenta2)

cliente2 = Cliente("67890", "Maria Lopez")
cuenta3 = Cuenta("0003", "ahorros", 1500)
cliente2.agregar_cuenta(cuenta3)

banco = Banco("Banco Central")
banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)

print(banco)
print(banco.ver_info_clientes())
print(f'Total saldos en cuentas de ahorros: {banco.total_saldos_ahorros()}')
print(f'Total saldos en cuentas corrientes: {banco.total_saldos_corriente()}')

# Cambiar el nombre del banco
banco.cambiar_nombre("Nuevo Banco Central")
print(banco)

"""