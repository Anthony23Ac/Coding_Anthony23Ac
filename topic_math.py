###
# 03 - SymPy y resolución de ecuaciones
# SymPy es una librería de Python para realizar matemáticas simbólicas.
# Permite trabajar con variables, expresiones algebraicas y ecuaciones.
# Para instalarla: python -m pip install sympy
###

from sympy import symbols, solve, Eq


###
# 01 - symbols()
# `symbols()` crea variables matemáticas simbólicas.
# A diferencia de una variable normal, SymPy puede manipularla algebraicamente.
###

x = symbols("x")
y = symbols("y")


###
# 02 - Expresiones algebraicas
# Podemos utilizar las variables simbólicas para crear expresiones matemáticas.
# `2*x + 5` representa matemáticamente: 2x + 5.
###

expression = 2*x + 5
print(expression)


###
# 03 - Eq()
# `Eq()` representa una igualdad matemática.
# Su estructura es: Eq(lado_izquierdo, lado_derecho)
# Por ejemplo: Eq(2*x + 5, 15) representa 2x + 5 = 15.
###

equation = Eq(2*x + 5, 15)
print(equation)


###
# 04 - solve()
# `solve()` sirve para resolver ecuaciones y despejar variables.
# Su estructura es: solve(ecuacion, variable)
# La variable que colocamos al final indica qué queremos despejar.
###

solution = solve(Eq(2*x + 5, 15), x)
print(solution)  # [5]


###
# 05 - ¿Por qué aparece x en solve()?
# En `solve(equation, x)`, la `x` significa "quiero encontrar x".
# Si queremos despejar y, escribiríamos: solve(equation, y).
###

solution = solve(Eq(2*x + 5, 15), x)
print(solution)


###
# 06 - Listas devueltas por solve()
# `solve()` normalmente devuelve una lista con las soluciones.
# `[5]` significa que existe una solución y su valor es 5.
# `[2, 3]` significa que existen dos soluciones.
###

solution = solve(x**2 - 5*x + 6, x)
print(solution)  # [2, 3]


###
# 07 - [0]
# `[0]` obtiene el primer elemento de una lista.
# Si solve() devuelve [5], solve(...)[0] devuelve solamente 5.
###

solution = solve(Eq(2*x + 5, 15), x)[0]
print(solution)  # 5


###
# 08 - Función lineal
# Una función lineal puede escribirse como: f(x) = mx + b.
# `m` representa la pendiente y `b` representa el intercepto con el eje Y.
# `x` es la variable independiente y f(x) o y es el resultado.
###

m = 2
b = 3

print(f"f(x) = {m}x + {b}")


###
# 09 - Pendiente
# Con dos puntos (x1, y1) y (x2, y2), calculamos la pendiente con:
# m = (y2 - y1) / (x2 - x1)
# Los paréntesis son importantes para respetar la fórmula matemática.
###

x1 = 2
y1 = 5

x2 = 6
y2 = 13

slope = (y2 - y1) / (x2 - x1)

print(slope)  # 2.0


###
# 10 - Forma punto-pendiente
# Una recta puede expresarse como:
# y - y1 = m(x - x1)
# Esta forma permite construir una función a partir de un punto y una pendiente.
###

equation = Eq(y - y1, slope * (x - x1))

print(equation)


###
# 11 - Despejar y automáticamente
# `solve(equation, y)` le indica a SymPy que queremos despejar y.
# `[0]` obtiene la primera solución de la lista.
###

linear_function = solve(
    Eq(y - y1, slope * (x - x1)),
    y
)[0]

print(linear_function)


###
# 12 - Resultado de la función
# Si los puntos son (2, 5) y (6, 13), obtenemos:
# f(x) = 2x + 1
###

print(f"f(x) = {linear_function}")


###
# 13 - subs()
# `subs()` significa substitute y sirve para sustituir un valor dentro
# de una expresión matemática.
# Su estructura es: expresion.subs(variable, valor)
###

result = linear_function.subs(x, 5)

print(result)  # 11


###
# 14 - Evaluar f(x)
# Si f(x) = 2x + 1 y queremos calcular f(5):
# sustituimos x por 5.
# Matemáticamente: f(5) = 2(5) + 1 = 11.
###

x_value = 5

function_value = linear_function.subs(x, x_value)

print(f"f({x_value}) = {function_value}")


###
# 15 - Pedir x al usuario
# Podemos utilizar input() para permitir que el usuario decida qué valor
# de x quiere utilizar.
# `float()` convierte el texto introducido por el usuario en un número decimal.
###

x_value = float(input("Enter a value for x: "))

function_value = linear_function.subs(x, x_value)

print(f"f({x_value}) = {function_value}")


###
# 16 - Intercepto con el eje Y
# El corte con el eje Y ocurre cuando x = 0.
# Por eso utilizamos: expression.subs(x, 0)
###

y_intercept = linear_function.subs(x, 0)

print(f"Y intercept: {y_intercept}")


###
# 17 - Intercepto con el eje X
# El corte con el eje X ocurre cuando y = 0.
# Como y = f(x), debemos resolver f(x) = 0.
# `solve(linear_function, x)` encuentra automáticamente ese valor de x.
###

x_intercept = solve(linear_function, x)[0]

print(f"X intercept: {x_intercept}")


###
# 18 - Diferencia entre los interceptos
# Eje Y -> x = 0 -> sustituimos x por 0.
# Eje X -> y = 0 -> resolvemos la función para encontrar x.
###

y_intercept = linear_function.subs(x, 0)
x_intercept = solve(linear_function, x)[0]

print(f"Y intercept: {y_intercept}")
print(f"X intercept: {x_intercept}")


###
# 19 - Buscar x cuando f(x) tiene otro valor
# Si queremos saber qué x produce un valor determinado de y,
# debemos resolver una ecuación como: f(x) = 5.
# Para eso utilizamos Eq(linear_function, 5).
###

x_result = solve(
    Eq(linear_function, 5),
    x
)[0]

print(x_result)


###
# 20 - ¿Por qué aparece x otra vez?
# En solve(Eq(linear_function, 5), x), el 5 es el valor que conocemos.
# La x final indica que queremos descubrir qué valor debe tener x.
###

x_result = solve(
    Eq(linear_function, 5),
    x
)[0]


###
# 21 - Permitir que el usuario elija y
# Podemos pedir al usuario el valor que queremos alcanzar en la función.
# Después SymPy encuentra automáticamente el x correspondiente.
###

y_value = float(input("Enter the value of y: "))

x_result = solve(
    Eq(linear_function, y_value),
    x
)[0]

print(f"When y = {y_value}, x = {x_result}")


###
# 22 - round()
# `round()` sirve para redondear números.
# round(numero) redondea al entero más cercano.
# round(numero, decimales) permite especificar cuántos decimales conservar.
###

number = 3.14159265

print(round(number))     # 3
print(round(number, 2))  # 3.14
print(round(number, 3))  # 3.142


###
# 23 - Redondear la pendiente
# Podemos redondear la pendiente para evitar demasiados decimales.
###

slope = round((y2 - y1) / (x2 - x1), 2)

print(f"Slope: {slope}")


###
# 24 - Redondear los interceptos
# También podemos redondear los resultados obtenidos mediante SymPy.
###

y_intercept = round(
    linear_function.subs(x, 0),
    2
)

x_intercept = round(
    solve(linear_function, x)[0],
    2
)


###
# 25 - Programa completo de función lineal
# El programa recibe dos puntos y calcula automáticamente:
# - Pendiente
# - Función lineal
# - Intercepto con el eje Y
# - Intercepto con el eje X
# - Valor de la función para cualquier x
###

from sympy import symbols, solve, Eq

x = symbols("x")
y = symbols("y")

print("")
print("--- PROGRAM FOR WORKING OUT A LINEAR FUNCTION ---")
print("")


# Primer punto
print("First location:")
x1 = float(input("Could you write x1? "))
y1 = float(input("Could you write y1? "))

# Segundo punto
print("Second location:")
x2 = float(input("Could you write x2? "))
y2 = float(input("Could you write y2? "))

print("")


# Calcular pendiente
slope = (y2 - y1) / (x2 - x1)


# Crear y despejar la función
linear_function = solve(
    Eq(y - y1, slope * (x - x1)),
    y
)[0]


# Intercepto con Y
y_intercept = round(
    linear_function.subs(x, 0),
    2
)


# Intercepto con X
x_intercept = round(
    solve(linear_function, x)[0],
    2
)


# Mostrar resultados
print(f"Slope: {round(slope, 2)}")
print(f"Linear function: y = {linear_function}")
print(f"Y intercept: {y_intercept}")
print(f"X intercept: {x_intercept}")


# Evaluar la función
x_value = float(input("Enter a value for x: "))

function_value = linear_function.subs(x, x_value)

print(f"f({x_value}) = {function_value}")

###
# symbols() -> crea variables matemáticas
# Eq()     -> crea una igualdad
# solve()  -> resuelve y despeja una variable
# [0]      -> obtiene el primer resultado de una lista
# subs()   -> sustituye un valor
# round()  -> redondea un número
#
# Pendiente:
# m = (y2 - y1) / (x2 - x1)
#
# Función lineal:
# f(x) = mx + b
#
# Corte con eje Y:
# x = 0
#
# Corte con eje X:
# f(x) = 0
#
# Evaluar función:
# f(x_value) -> expression.subs(x, x_value)
###