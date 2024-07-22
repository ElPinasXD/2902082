import math

# Funciones trigonométricas:

# seno
angulo_en_radianes = 0.5
valor_seno = math.sin(angulo_en_radianes)
print(f"El seno de {angulo_en_radianes} es: {valor_seno}")

# coseno
angulo_en_radianes = 0.5
valor_coseno = math.cos(angulo_en_radianes)
print(f"El coseno de {angulo_en_radianes} es: {valor_coseno}")

# tangente
angulo_en_radianes = 0.5
valor_tangente = math.tan(angulo_en_radianes)
print(f"La tangente de {angulo_en_radianes} es: {valor_tangente}")

# arcocoseno
valor_coseno = 0.866
angulo_en_radianes = math.acos(valor_coseno)
print(f"El arcocoseno de {valor_coseno} es: {angulo_en_radianes}")

# arcoseno
valor_seno = 0.5
angulo_en_radianes = math.asin(valor_seno)
print(f"El arcoseno de {valor_seno} es: {angulo_en_radianes}")

# arctangente
valor_tangente = 1.0
angulo_en_radianes = math.atan(valor_tangente)
print(f"La arctangente de {valor_tangente} es: {angulo_en_radianes}")

# arctangente2
coordenada_y = 3
coordenada_x = 4
angulo_en_radianes = math.atan2(coordenada_y, coordenada_x)
print(f"La arctangente de {coordenada_y} con respecto a {coordenada_x} es: {angulo_en_radianes}")





# Funciones exponenciales y logarítmicas:

# exponencial
base = 2
exponente = 3
resultado_exponencial = math.pow(base, exponente)
print(f"{base} elevado a la potencia {exponente} es: {resultado_exponencial}")

# logaritmo natural
numero = 10
resultado_logaritmo = math.log(numero)
print(f"El logaritmo natural de {numero} es: {resultado_logaritmo}")

# logaritmo en base 10
numero = 100
resultado_logaritmo = math.log10(numero)
print(f"El logaritmo en base 10 de {numero} es: {resultado_logaritmo}")




# Otras funciones matemáticas:

# valor absoluto
numero = -5.2
valor_absoluto = math.fabs(numero)
print(f"El valor absoluto de {numero} es: {valor_absoluto}")

# raíz cuadrada
numero = 9
raiz_cuadrada = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")

# redondeo hacia arriba
numero = 4.8
numero_redondeado = math.ceil(numero)
print(f"El número {numero} redondeado hacia arriba es: {numero_redondeado}")

# redondeo hacia abajo
numero = 4.8
numero_redondeado = math.floor(numero)
print(f"El número {numero} redondeado hacia abajo es: {numero_redondeado}")

# potencia entera
base = 2
exponente = 3
resultado_potencia_entera = math.pow(base, base ** exponente % 2)
print(f"{base} elevado a la potencia {exponente} con módulo 2 es: {resultado_potencia_entera}")

# grados a radianes
grados = 45
angulo_en_radianes = math.radians(grados)
print(f"Convertir {grados} grados a radianes es: {angulo_en_radianes}")

# radianes a grados
angulo_en_radianes = 0.785
grados = math.degrees(angulo_en_radianes)
print(f"Convertir {angulo_en_radianes} radianes a grados es: {grados}")
