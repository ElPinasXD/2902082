"""
    etiqueta2 = tk.Label(ventana_principal, text="3028379495")
etiqueta3 = tk.Label(ventana_principal, text="estebanpineros42@gmail.com")
etiqueta2.pack()
etiqueta3.pack()


import tkinter as tk

ventana_principal = tk.Tk()
etiqueta = tk.Label(ventana_principal, text="Esteban Piñeros") # Muestra el texto en la ventana
etiqueta.pack() #Ajusta la ventana al contenido que tiene  
ventana_principal.title("Aplicacion movil") # Titulo de la ventana
ventana_principal.geometry("10x10000+100+1") #anchoxalto+left+top
ventana_principal.resizable(False, True) # Para modificar si una ventana puede ser redimensionada por el usuario
ventana_principal.attributes("-alpha", 0.5) # Traspariencia 
ventana_principal.mainloop() # Entra en un bucle que mantiene la ventana abierta




import tkinter as tk
from tkinter.messagebox import showinfo 
from tkinter.messagebox import showerror
from tkinter.messagebox import showwarning

ventana_principal = tk.Tk()
showinfo(title="Mensaje", message="Bienvenido a la grasa") # Ventana emergente informativa
showerror(title="Error", message="Tienes un virus") # Ventana emergente con error
showwarning(title="advertencia", message="Estas seguro") # Ventana emergente con advertencia
ventana_principal.mainloop()



import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo

ventana_principal = tk.Tk()
ventana_principal.title("Troll XD")

seleccion = askyesno(title="One Question", message="¿Sus papas saben que usted es gay? 🤪") # Ventana emergente con opciones
if seleccion:
    ventana_principal.destroy # Si = Desaperece la ventana
else: 
    showinfo(title="Menseja", message="Troleado puto XD") # No = Crea otra ventana con un mensaje 
ventana_principal.mainloop()

"""

# Hacer un custornario de true or false y que al final le diga su puntaje (Falta mi version)

import tkinter as tk
from tkinter.messagebox import askyesno, showerror, showinfo

ventana_principal = tk.Tk()
ventana_principal.title("Preguntas")

seleccion = askyesno(title="Primera Pregunta", message="2 + 2 = 4") 
if seleccion:
    ventana_principal.destroy 
else: 
    showerror(title="Error", message="Respuesta Incorrecta ") 
     
seleccion = askyesno(title="Segunda Pregunta", message="¿El cielo es azul?") 
if seleccion:
    ventana_principal.destroy 
else: 
    showerror(title="Error", message="Respuesta Incorrecta ") 

seleccion = askyesno(title="Tercera Pregunta", message="El uniforme del sena tiene chaqueta blanca?") 
if seleccion:
    showerror(title="Error", message="Respuesta Incorrecta ")
else: 
     ventana_principal.destroy 
     
seleccion = askyesno(title="Cuarta Pregunta", message="1 + 1 = 3") 
if seleccion:
    showerror(title="Error", message="Respuesta Incorrecta ")
else: 
     ventana_principal.destroy 
     
seleccion = askyesno(title="Quinta Pregunta", message="El avion vuela?") 
if seleccion:
    ventana_principal.destroy 
else: 
    showerror(title="Error", message="Respuesta Incorrecta ") 


ventana_principal.mainloop()

import tkinter as tk
from tkinter.messagebox import askyesno, showerror, showinfo

def hacer_pregunta(pregunta, respuesta_correcta):
    respuesta = askyesno(title="Pregunta", message=pregunta)
    respuestas.append(respuesta == respuesta_correcta)

def finalizar_preguntas():
    ventana_principal.destroy()
    mostrar_resultado()

def mostrar_resultado():
    respuestas_correctas = respuestas.count(True)
    total_preguntas = len(respuestas)
    puntuacion = f"Tienes {respuestas_correctas} de {total_preguntas} respuestas correctas"
    showinfo(title="Resultado", message=puntuacion)

ventana_principal = tk.Tk()
ventana_principal.title("Preguntas")

respuestas = []

# Se agregan las preguntas en el orden deseado
hacer_pregunta("2 + 2 = 4", True)
hacer_pregunta("¿El cielo es azul?", True)
hacer_pregunta("El uniforme del sena tiene chaqueta blanca?", False)
hacer_pregunta("1 + 1 = 3", False)
hacer_pregunta("El avión vuela?", True)

# Se termina y muestra los resultados después de las preguntas
ventana_principal.after(100, finalizar_preguntas)

ventana_principal.mainloop()


"""

import tkinter as tk
from tkinter.messagebox import askyesno, showinfo

ventana_principal = tk.Tk()
ventana_principal.title("Cuestionario")

respuestas = []

def hacer_pregunta(pregunta, respuesta_correcta):
    respuesta = askyesno(title="Pregunta", message=pregunta)
    respuestas.append(respuesta == respuesta_correcta)

hacer_pregunta("2 + 2 = 4", True)  
hacer_pregunta("¿El cielo es azul?", True)  
hacer_pregunta("El uniforme del Sena tiene chaqueta blanca?", True)  
hacer_pregunta("1 + 1 = 3", False)  
hacer_pregunta("El avión vuela?", True)  

def mostrar_resultado():
    respuestas_correctas = respuestas.count(True)
    total_preguntas = len(respuestas)
    puntuacion = f"Tienes {respuestas_correctas} de {total_preguntas} respuestas correctas"
    showinfo(title="Resultado", message=puntuacion)
    ventana_principal.destroy()

ventana_principal.after(100, mostrar_resultado)

ventana_principal.mainloop()
"""