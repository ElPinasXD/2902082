"""
self = Se tiene una referencia al objeto actual que está haciendo uso de los miembros de la clase
__init__ () = Para definir el constructor de una clase
__ str__ () = tiene el comportamiento por defecto de retornar una cadena con la clase a la que pertenece el objeto y su dirección de memoria


class Persona: # Crear Clase
  def __init__(self, ced, nom, ed): # Definir constructor con parametros 
    print ("Me estoy creando ", self) 
    self.cedula = ced 
    self.nombre = nom 
    self.edad = ed 

obj1 = Persona(123, "Luis", 35) # Creamos objetos de la clase
obj2 = Persona(345, "Lina", 20)
print (obj1.cedula, obj1.nombre, obj1.edad)
print(obj1)
print (obj2.cedula, obj2.nombre, obj2.edad)
print(obj2)


-----------------------------------------------------------------------------------------------------------------


Atributos de instancia = esto quiere decir que cada instancia (objeto) tiene su propio conjunto 
de atributos con sus propios valores

Atributos de clase = cuyo valor es el mismo para todas las instancias de una clase pues 
pertenece a la clase y no a sus instancias, aunque estas lo puedan acceder

Métodos de Clase (@classmethod) = Es un método que tiene acceso a la clase (atributos de clase u otros métodos de clase)

Metodos estaticos (@staticmethod) = Son métodos que cumplen una función particular y que quedan asociados a una determinada clase


"""